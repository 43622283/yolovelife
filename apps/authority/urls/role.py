# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import role

urlpatterns = [
    path(r'v1/role/', role.RoleListAPI.as_view()),
    path(r'v1/role/create/', role.RoleCreateAPI.as_view()),
    path(r'v1/role/update/', role.RoleUpdateAPI.as_view()),
    path(r'v1/role/<int:pk>/user/', role.RoleUserAPI.as_view()),
    path(r'v1/role/<int:pk>/user/add/', role.RoleUserAddAPI.as_view()),
    path(r'v1/role/<int:pk>/user/remove/', role.RoleUserRemoveAPI.as_view()),
    path(r'v1/role/<int:pk>/api/', role.RoleAPIAPI.as_view()),
    path(r'v1/role/<int:pk>/api/add/', role.RoleAPIAddAPI.as_view()),
    path(r'v1/role/<int:pk>/api/remove/', role.RoleAPIRemoveAPI.as_view()),
    path(r'v1/role/<int:pk>/page/', role.RolePageAPI.as_view()),
    path(r'v1/role/<int:pk>/page/add/', role.RolePageAddAPI.as_view()),
    path(r'v1/role/<int:pk>/page/remove/', role.RolePageRemoveAPI.as_view()),
]
