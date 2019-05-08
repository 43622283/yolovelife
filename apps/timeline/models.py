# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from django.contrib.auth.models import Group
from django.db import models
import uuid
from scene.models import WorkOrder, AssetChange


class AbstractHistory(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False)
    type = models.IntegerField(default=0)
    msg = models.TextField(default='')
    create_time = models.DateTimeField(auto_now_add=True,)

    class Meta:
        abstract = True


class RoleHistory(AbstractHistory):
    instances = models.ManyToManyField(Group, default=None, blank=True, related_name='role_history')


class AssetHistory(AbstractHistory):
    instances = models.ManyToManyField(AssetChange, default=None, blank=True, related_name='asset_history')


class History(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False)
    type = models.IntegerField(default=0)
    msg = models.TextField(default='')
    time = models.DateTimeField(auto_now_add=True,)


class SceneHistory(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False)
    type = models.IntegerField(default=0)#历史类型
    msg = models.TextField(default='')#信息
    time = models.DateTimeField(auto_now_add=True,)#历史时间

    workorder = models.ForeignKey(WorkOrder, default=None, blank=True, null=True,
                                    on_delete=models.SET_NULL, related_name='history')
