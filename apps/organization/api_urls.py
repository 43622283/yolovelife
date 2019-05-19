# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-3
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from .api import department as department_api
from .api import user as user_api
urlpatterns = [
    # Resource depart api
    path(r'v2/department/list/', department_api.OrganizationDepartmentListAPI.as_view()),
    path(r'v2/user/<uuid:pk>/list/', user_api.OrganizationUserListAPI.as_view()),
]
