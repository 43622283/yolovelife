# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-12-10
# Author Yo
# Email YoLoveLife@outlook.com
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings
from deveops.utils.uuid_maker import uuid_maker
from django.contrib.auth.models import Group
from authority.models import ExtendUser


__all__ = [
    'Notice', 'Remind'
]


class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid_maker, editable=False)

    create_time = models.DateTimeField(auto_now_add=True)

    type = models.IntegerField(default=settings.STATUS_NOTICE_ONCALL)

    title = models.CharField(default='', max_length=1000)
    description = models.CharField(default='', max_length=1000)

    users = models.ManyToManyField(ExtendUser, blank=True, related_name='notifys', verbose_name=_("notifys"))

    groups = models.ManyToManyField(Group, blank=True, related_name='notifys', verbose_name=_("notifys"))

    visible = models.BooleanField(default=False)

    class Meta:
        ordering = ['create_time', ]


class Remind(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid_maker, editable=False)

    create_time = models.DateTimeField(auto_now_add=True)

    type = models.IntegerField(default=settings.STATUS_REMIND_SUCCESS)

    title = models.CharField(default='', max_length=1000)
    description = models.CharField(default='', max_length=1000)

    users = models.ManyToManyField(ExtendUser, blank=True, related_name='reminds', verbose_name=_("notifys"))

    groups = models.ManyToManyField(Group, blank=True, related_name='reminds', verbose_name=_("notifys"))

    visible = models.BooleanField(default=False)

    class Meta:
        ordering = ['create_time', ]
