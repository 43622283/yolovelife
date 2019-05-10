# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-3
# Author Yo
# Email YoLoveLife@outlook.com
from django.utils.translation import ugettext_lazy as _
from django.db import models
from deveops.utils.uuid_maker import uuid_maker
from django.conf import settings
from deveops.utils.uuid_maker import uuid_maker
__all__ = [

]


class Dashboard(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid_maker, editable=False)

    class Meta:
        permissions = (
            ('deveops_page_dashboard', u'跳板机页面'),
        )