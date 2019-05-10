# -*- coding:utf-8 -*-
from django.db import models
import socket
from manager.models import Group,Host
from deveops.utils import aes
from deveops.utils.uuid_maker import uuid_maker
from django.conf import settings
from zdb.tasks import database_single_flush

__all__ = [
    'RedisInstance', 'DBInstance', 'DBDatabase',
]


class RedisInstance(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid_maker, editable=False)
    name = models.CharField(max_length=100, default='undefined')
    host = models.CharField(max_length=200, default='localhost')
    port = models.CharField(max_length=5, default='3306')
    _passwd = models.CharField(max_length=1000, default='', null=True, blank=True)

    @property
    def password(self):
        if self._passwd:
            return aes.decrypt(self._passwd)
        else:
            return 'nopassword'

    @password.setter
    def password(self, password):
        self._passwd = aes.encrypt(password).decode()


class DBInstance(models.Model):
    INSTANCE_STATUS = (
        (settings.STATUS_DB_INSTANCE_PASSWORD_WRONG, '密码错误'),
        (settings.STATUS_DB_INSTANCE_CONNECT_REFUSE, '连接拒绝'),
        (settings.STATUS_DB_INSTANCE_UNREACHABLE, '不可到达'),
        (settings.STATUS_DB_INSTANCE_CAN_BE_USE, '正常'),
    )
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid_maker, editable=False)

    name = models.CharField(max_length=100, default='undefined')
    connect_address = models.CharField(max_length=200, default='localhost')
    port = models.CharField(max_length=5, default='3306')
    is_master = models.BooleanField(default=True)
    user = models.CharField(max_length=20, default='adminroot')
    _passwd = models.CharField(max_length=1000, default='', null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    _status = models.IntegerField(default=settings.STATUS_DB_INSTANCE_UNREACHABLE, choices=INSTANCE_STATUS)


    @property
    def password(self):
        if self._passwd:
            return aes.decrypt(self._passwd)
        else:
            return 'nopassword'

    @password.setter
    def password(self, password):
        self._passwd = aes.encrypt(password).decode()

    def check_status(self):
        database_single_flush.delay(self)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self.check_status()


class DBDatabase(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid_maker, editable=False)
    instance = models.ForeignKey(DBInstance, on_delete=models.SET_NULL, null=True, related_name='databases')
    name = models.CharField(max_length=500, default='undefined')

