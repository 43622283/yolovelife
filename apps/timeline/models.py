# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from django.contrib.auth.models import Group
from django.db import models
from deveops.utils.uuid_maker import uuid_maker
from deveops.models import BaseModal

from scene.models import WorkOrder, AssetChange
from utils.models import FILE, IMAGE
from authority.models import Jumper, Key, ExtendUser
from kalendar.models import Kalendar


class AbstractHistory(BaseModal):
    type = models.IntegerField(default=0)
    msg = models.TextField(default='')
    create_time = models.DateTimeField(auto_now_add=True,)

    class Meta:
        abstract = True


class UserHistory(AbstractHistory):
    instances = models.ManyToManyField(ExtendUser, default=None, blank=True, related_name='user_history')


class JumperHistory(AbstractHistory):
    instances = models.ManyToManyField(Jumper, default=None, blank=True, related_name='jumper_history')


class KeyHistory(AbstractHistory):
    instances = models.ManyToManyField(Key, default=None, blank=True, related_name='key_history')


class FileHistory(AbstractHistory):
    instances = models.ManyToManyField(FILE, default=None, blank=True, related_name='file_history')


class ImageHistory(AbstractHistory):
    instances = models.ManyToManyField(IMAGE, default=None, blank=True, related_name='image_history')


class RoleHistory(AbstractHistory):
    instances = models.ManyToManyField(Group, default=None, blank=True, related_name='role_history')


class KalendarHistory(AbstractHistory):
    instances = models.ManyToManyField(Kalendar, default=None, blank=True, related_name='kalendar_history')


class AssetHistory(AbstractHistory):
    instances = models.ManyToManyField(AssetChange, default=None, blank=True, related_name='asset_history')


class WorkOrderHistory(AbstractHistory):
    instances = models.ManyToManyField(WorkOrder, default=None, blank=True, related_name='workorder_history')
