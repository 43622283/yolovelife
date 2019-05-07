# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import jumper

urlpatterns = [
    path(r'v1/jumper/', jumper.JumperListAPI.as_view()),
    path(r'v1/jumper/bypage/', jumper.JumperListByPageAPI.as_view()),
    path(r'v1/jumper/<uuid:pk>/status/', jumper.JumperStatusAPI.as_view()),
    path(r'v1/jumper/create/', jumper.JumperCreateAPI.as_view()),
    path(r'v1/jumper/<uuid:pk>/update/', jumper.JumperUpdateAPI.as_view()),
    path(r'v1/jumper/<uuid:pk>/delete/', jumper.JumperDeleteAPI.as_view()),
]
