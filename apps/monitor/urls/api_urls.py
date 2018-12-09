# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import monitor as MonitorAPI
urlpatterns = [
    # Resource host api
    path(r'v1/host/<uuid:pk>/cpu/aliyun/byuuid/<int:time>/', MonitorAPI.MonitorHostAliyunDetailCPUAPI.as_view()),
    path(r'v1/host/<uuid:pk>/memory/aliyun/byuuid/<int:time>/', MonitorAPI.MonitorHostAliyunDetailMemoryAPI.as_view()),
    path(r'v1/host/<uuid:pk>/disk/read/aliyun/byuuid/<int:time>/', MonitorAPI.MonitorHostAliyunDetailIReadIOPS.as_view()),
    path(r'v1/host/<uuid:pk>/internet/in/aliyun/byuuid/<int:time>/', MonitorAPI.MonitorHostAliyunDetailInternetInRate.as_view()),
    path(r'v1/host/<uuid:pk>/disk/use/aliyun/byuuid/<int:time>/', MonitorAPI.MonitorHostAliyunDetailDiskUse.as_view()),
    path(r'v1/host/<uuid:pk>/1mload/aliyun/byuuid/<int:time>/', MonitorAPI.MonitorHostAliyunDetailLoad1m.as_view()),
    path(r'v1/host/<uuid:pk>/5mload/aliyun/byuuid/<int:time>/', MonitorAPI.MonitorHostAliyunDetailLoad5m.as_view()),
    path(r'v1/host/<uuid:pk>/15mload/aliyun/byuuid/<int:time>/', MonitorAPI.MonitorHostAliyunDetailLoad15m.as_view()),
]