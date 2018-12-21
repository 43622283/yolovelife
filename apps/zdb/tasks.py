# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
from celery.task import periodic_task
from celery.schedules import crontab
from django.db.models import Q
import celery
import MySQLdb
from django.conf import settings
import socket
from zdb import models
from celery import Task, task


class ZDBTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))


@task(base=ZDBTask)
def status_flush(instance):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(settings.SSH_TIMEOUT)
    try:
        s.connect((str(instance.connect_address), int(instance.port)))
        print(instance.connect_address, instance.port)
    except socket.timeout as e:
        print('timeout')
        instance._status = settings.STATUS_DB_INSTANCE_UNREACHABLE
        instance.save()
        return
    except ConnectionRefusedError as e:
        print('refuse')
        instance._status = settings.STATUS_DB_INSTANCE_CONNECT_REFUSE
        instance.save()
        return
    except Exception as e:
        print('exception')
        instance._status = settings.STATUS_DB_INSTANCE_UNREACHABLE
        instance.save()
        return

    try:
        db = MySQLdb.connect(
            host=instance.connect_address,
            port=instance.port,
            user=instance.user,
            password=instance.password
        )
    except MySQLdb.connections.OperationalError as e:
        instance._status = settings.STATUS_DB_INSTANCE_PASSWORD_WRONG
        instance.save()
        return

    instance._status = settings.STATUS_DB_INSTANCE_CAN_BE_USE
    instance.save()


def get_database_list(instance):
    try:
        conn = MySQLdb.connect(
            host=instance.connect_address,
            port=int(instance.port),
            user=instance.user,
            password=instance.password,
            charset='utf8'
        )
        cursor = conn.cursor()
        sql = "show databases"
        cursor.execute(sql)
        list_db = [row[0] for row in cursor.fetchall()
                  if row[0] not in ('information_schema', 'performance_schema', 'mysql', 'sys', 'test')]
        return list_db
    except Exception as e:
        print(e)
        return []


@task(base=ZDBTask)
def database_single_flush(instance):
    list_db = get_database_list(instance)
    for db in list_db:
        if not instance.databases.filter(name=db).exists():
            obj = models.DBDatabase.objects.create(
                name=db
            )
            instance.databases.add(obj)
            instance.save()

@periodic_task(run_every=settings.ZDB_INSTANCE_FLUSH)
def instance_flush():
    pass

@periodic_task(run_every=settings.ZDB_DATABASE_FLUSH)
def database_flush():
    for instance in models.DBInstance.objects.filter(_status=settings.STATUS_DB_INSTANCE_CAN_BE_USE):
        list_db = get_database_list(instance)
        for db in list_db:
            if not instance.databases.filter(name=db).exists():
                obj = models.DBDatabase.objects.create(
                    name=db
                )
                instance.databases.add(obj)
                instance.save()
