# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-3
# Author Yo
# Email YoLoveLife@outlook.com
from django.db import models
import django.utils.timezone as timezone
from django.conf import settings
from deveops.models import BaseModal

__all__ = [
    'Kalendar'
]


class Kalendar(BaseModal):
    time = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(default=settings.STATUS_KALENDAR_NOTICE)
    title = models.CharField(default='', max_length=200)
    description = models.CharField(default='', max_length=500)

    class Meta:
        permissions = (
            ('deveops_page_kalendar', u'日历页面'),
            ('deveops_api_list_kalendar', u'罗列日历'),
            ('deveops_api_update_kalendar', u'更新日历'),
            ('deveops_api_create_kalendar', u'新建日历'),
            ('deveops_api_delete_kalendar', u'删除日历'),
        )
