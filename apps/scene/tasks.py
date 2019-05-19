# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
import json
from datetime import date, timedelta
from celery.task import periodic_task
from django_redis import get_redis_connection
from django.conf import settings
from authority.models import ExtendUser
from celery import Task, task
from scene.models import Record, WorkOrder


class ReportTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))


@task(base=ReportTask)
def report_day(user_id):
    conn = get_redis_connection('report')
    report_dict = dict()
    user_obj = ExtendUser.objects.get(id=user_id)
    start_time = date.today()
    end_time = date.today() + timedelta(days=1)
    workorder_queryset = user_obj.workorders.filter(create_time__range=(start_time, end_time))
    report_dict['start_time'] = start_time.strftime('%Y-%m-%d')
    report_dict['user'] = user_obj.full_name
    report_dict['workorder_count'] = workorder_queryset.count()
    report_dict['workorder_inactive'] = workorder_queryset.filter(_status=settings.TYPE_WORKORDER_INACTIVE).count()
    report_dict['workorder_run'] = workorder_queryset.filter(_status=settings.TYPE_WORKORDER_RUN).count()
    report_dict['workorder_done'] = workorder_queryset.filter(_status=settings.TYPE_WORKORDER_DONE).count()

    conn.set('REPORT_{0}_{1}'.format(start_time.strftime('%Y-%m-%d'), user_id), json.dumps(report_dict))


@task(base=ReportTask)
def report_week(user_id):
    pass


@task(base=ReportTask)
def report_month(user_id):
    pass


@periodic_task(run_every=settings.WORKORDER_RECORD)
def record():
    for record in Record.objects.filter(solved=False):
        record.workorder()