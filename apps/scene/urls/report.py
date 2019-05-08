# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import report as ReportAPI

urlpatterns = [
    # Resource report api
    path(r'v1/report/day/', ReportAPI.SceneReportDayAPI.as_view()),
    path(r'v1/report/week/', ReportAPI.SceneReportDayAPI.as_view()),
]
