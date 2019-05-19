# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import user

urlpatterns = [
    path(r'v2/login/', user.UserLoginAPI.as_view()),
    path(r'v2/userinfo/', user.UserInfoAPI.as_view()),
    path(r'v2/user/list/', user.UserListAPI.as_view()),
    path(r'v2/user/create/', user.UserCreateAPI.as_view()),
    path(r'v2/user/<uuid:pk>/update/', user.UserUpdateAPI.as_view()),
    path(r'v2/user/<uuid:pk>/delete/', user.UserDeleteAPI.as_view()),
    path(r'v2/user/qrcode/', user.UserQRCodeAPI.as_view()),
    path(r'v2/user/expire/', user.UserExpireAPI.as_view()),
]
