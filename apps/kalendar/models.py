# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-3
# Author Yo
# Email YoLoveLife@outlook.com
from django.utils.translation import ugettext_lazy as _
from django.db import models
import django.utils.timezone as timezone
from django.conf import settings
import uuid
__all__ = [

]


class Kalendar(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False)

    time = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(default=settings.STATUS_KALENDAR_NOTICE)
    title = models.CharField(default='', max_length=1000)
    description = models.CharField(default='', max_length=1000)
