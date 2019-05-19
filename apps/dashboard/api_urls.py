# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-3
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from . import api as DashboardAPI
urlpatterns = [
    path(r'v2/workorder/', DashboardAPI.DashboardWorkOrderAPI.as_view()),
]
