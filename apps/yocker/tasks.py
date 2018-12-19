# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com

from __future__ import absolute_import, unicode_literals
from celery import Task,task
from dns import resolver
import time
from django.conf import settings
from deveops.tools.aliyun_v2.request.cdn import AliyunCDNTool
from deveops.tools.qiniu.cdn import QiNiuCDNTool
