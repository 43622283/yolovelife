# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import key

urlpatterns = [
    path(r'v1/key/', key.KeyListAPI.as_view()),
    path(r'v1/key/bypage/', key.KeyListByPageAPI.as_view()),
    path(r'v1/key/create/', key.KeyCreateAPI.as_view()),
    path(r'v1/key/<uuid:pk>/update/', key.KeyUpdateAPI.as_view()),
    path(r'v1/key/<uuid:pk>/delete/', key.KeyDeleteAPI.as_view()),
]
