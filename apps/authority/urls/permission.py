# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import permission

urlpatterns = [
    path(r'v1/permission/api/', permission.PermissionAPIListAPI.as_view()),
    path(r'v1/permission/page/', permission.PermissionPageListAPI.as_view()),
]
