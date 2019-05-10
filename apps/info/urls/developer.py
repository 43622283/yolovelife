# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import developer as DEVELOPERAPI

urlpatterns = [
    path(r'v1/developer/list/', DEVELOPERAPI.INFODEVELOPERListAPI.as_view()),
    path(r'v1/developer/create/', DEVELOPERAPI.INFODEVELOPERCreateAPI.as_view()),
    path(r'v1/developer/<uuid:pk>/delete/', DEVELOPERAPI.INFODEVELOPERDeleteAPI.as_view()),
]
