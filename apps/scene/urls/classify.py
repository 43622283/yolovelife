# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import classify as ClassifyAPI

urlpatterns = [
    path(r'v2/classify/list/', ClassifyAPI.SceneClassifyListAPI.as_view()),
    path(r'v2/classify/create/', ClassifyAPI.SceneClassifyCreateAPI.as_view()),
    path(r'v2/classify/<uuid:pk>/delete/', ClassifyAPI.SceneClassifyDeleteAPI.as_view()),
]
