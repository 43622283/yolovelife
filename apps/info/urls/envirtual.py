# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import envirtual as ENVIRTUALAPI

urlpatterns = [
    path(r'v1/envirtual/', ENVIRTUALAPI.INFOENVIRTUALListAPI.as_view()),
    path(r'v1/envirtual/create/', ENVIRTUALAPI.INFOENVIRTUALCreateAPI.as_view()),
    path(r'v1/envirtual/<uuid:pk>/delete/', ENVIRTUALAPI.INFOENVIRTUALDeleteAPI.as_view()),
]
