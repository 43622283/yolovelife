# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import group

urlpatterns = [
    path(r'v1/group/', group.GroupListAPI.as_view()),
    path(r'v1/group/bypage/', group.GroupListByPageAPI.as_view()),
    path(r'v1/group/create/', group.GroupCreateAPI.as_view()),
    path(r'v1/group/<int:pk>/update/', group.GroupUpdateAPI.as_view()),
    path(r'v1/group/<int:pk>/delete/', group.GroupDeleteAPI.as_view()),
]
