# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import type as TYPEAPI

urlpatterns = [
    path(r'v2/type/list/', TYPEAPI.INFOTYPEListAPI.as_view()),
    path(r'v2/type/create/', TYPEAPI.INFOTYPECreateAPI.as_view()),
    path(r'v2/type/<uuid:pk>/delete/', TYPEAPI.INFOTYPEDeleteAPI.as_view()),
]
