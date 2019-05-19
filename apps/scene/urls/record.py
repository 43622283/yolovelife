# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import record as RecordAPI

urlpatterns = [
    path(r'v2/record/create/', RecordAPI.SceneRecordCreateAPI.as_view()),
]
