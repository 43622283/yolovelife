# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import user

urlpatterns = [
    path(r'login/', user.UserLoginAPI.as_view()),
    path(r'userinfo/', user.UserInfoAPI.as_view()),
    path(r'v1/user/', user.UserListAPI.as_view()),
    path(r'v1/user/bypage/', user.UserListByPageAPI.as_view()),
    path(r'v1/opsuser/', user.UserOpsListAPI.as_view()),
    path(r'v1/opsuser/bypage/', user.UserOpsListByPageAPI.as_view()),
    path(r'v1/workuser/', user.UserWorkListAPI.as_view()),
    path(r'v1/user/create/', user.UserCreateAPI.as_view()),
    path(r'v1/user/<int:pk>/update/', user.UserUpdateAPI.as_view()),
    path(r'v1/user/<int:pk>/delete/', user.UserDeleteAPI.as_view()),
    path(r'v1/user/qrcode/', user.UserQRCodeAPI.as_view()),
    path(r'v1/user/expire/', user.UserExpireAPI.as_view()),
]
