# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import info as INFOAPI

urlpatterns = [
    path(r'v1/info/', INFOAPI.INFOINFOListAPI.as_view()),
    path(r'v1/info/create/', INFOAPI.INFOINFOCreateAPI.as_view()),
    path(r'v1/info/<uuid:pk>/update/', INFOAPI.INFOINFOUpdateAPI.as_view()),
]
