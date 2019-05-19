# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-12-10
# Author Yo
# Email YoLoveLife@outlook.com
from __future__ import unicode_literals
from django.contrib.auth.models import Group
from django.db import models
from django.conf import settings
from deveops.models import BaseModal
from authority.models import ExtendUser


__all__ = [
    'Notice', 'Remind'
]


class Notice(BaseModal):
    create_time = models.DateTimeField(auto_now_add=True)
    type = models.IntegerField(default=settings.STATUS_NOTICE_ONCALL)
    title = models.CharField(default='', max_length=1000)
    description = models.CharField(default='', max_length=1000)
    users = models.ManyToManyField(ExtendUser, blank=True, related_name='notifys')
    roles = models.ManyToManyField(Group, blank=True, related_name='notifys')

    class Meta:
        ordering = ['create_time', ]

        permissions = (
            ('deveops_page_notice', u'注意页面'),
            ('deveops_api_list_notice', u'获取注意'),
            ('deveops_api_create_notice', u'新建注意'),
        )


class Remind(BaseModal):
    create_time = models.DateTimeField(auto_now_add=True)
    type = models.IntegerField(default=settings.STATUS_REMIND_SUCCESS)
    title = models.CharField(default='', max_length=1000)
    description = models.CharField(default='', max_length=1000)
    users = models.ManyToManyField(ExtendUser, blank=True, related_name='reminds')
    roles = models.ManyToManyField(Group, blank=True, related_name='reminds')

    class Meta:
        ordering = ['create_time', ]

        permissions = (
            ('deveops_page_remind', u'提醒页面'),
            ('deveops_api_list_remind', u'获取提醒'),
            ('deveops_api_create_remind', u'新建提醒'),
        )
