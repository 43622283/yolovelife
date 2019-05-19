# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import workorder as WorkOrderAPI

urlpatterns = [
    path(r'v2/workorder/list/', WorkOrderAPI.SceneWorkOrderListAPI.as_view()),
    path(r'v2/workorder/create/', WorkOrderAPI.SceneWorkOrderCreateAPI.as_view()),
    path(r'v2/workorder/mobile/detail/', WorkOrderAPI.SceneWorkOrderMobileDetailAPI.as_view()),
    path(r'v2/workorder/<uuid:pk>/detail/', WorkOrderAPI.SceneWorkOrderDetailAPI.as_view()),
    path(r'v2/workorder/<uuid:pk>/update/', WorkOrderAPI.SceneWorkOrderUpdateAPI.as_view()),
    path(r'v2/workorder/<uuid:pk>/active/', WorkOrderAPI.SceneWorkOrderActiveAPI.as_view()),
    path(r'v2/workorder/<uuid:pk>/appoint/', WorkOrderAPI.SceneWorkOrderAppointAPI.as_view()),
    path(r'v2/workorder/<uuid:pk>/done/', WorkOrderAPI.SceneWorkOrderDoneAPI.as_view()),
    path(r'v2/workorder/<uuid:pk>/comment/create/', WorkOrderAPI.SceneWorkOrderCommentAPI.as_view()),
]
