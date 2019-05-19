# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-3
# Author Yo
# Email YoLoveLife@outlook.com
import redis
import json
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import Response, status
from rest_framework.views import APIView
from django_redis import get_redis_connection
from deveops.api import WebTokenAuthentication

__all__ = [
    "DashboardWorkOrderAPI"
]


class DashboardWorkOrderAPI(WebTokenAuthentication, APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, *args, **kwargs):
        conn = get_redis_connection('dashboard')
        get_dict = dict()

        if conn.exists('WORKORDER_COUNT') and conn.exists('REPOSITORY_COUNT') \
            and conn.exists('WORKORDER_LAST') and conn.exists('MONTHS_COUNT'):

            WORKORDER_COUNT = conn.get('WORKORDER_COUNT')
            get_dict['count'] = json.loads(WORKORDER_COUNT)

            REPOSITORY_COUNT = conn.get('REPOSITORY_COUNT')
            get_dict['repository'] = json.loads(REPOSITORY_COUNT)

            WORKORDER_LAST = conn.get('WORKORDER_LAST')
            get_dict['workorder'] = json.loads(WORKORDER_LAST)

            MONTHS_COUNT = conn.get('MONTHS_COUNT')
            get_dict['months'] = json.loads(MONTHS_COUNT)

            TIMELINES = '[]'#conn.get('TIMELINES')
            get_dict['timelines'] = json.loads(TIMELINES)
        else:
            get_dict = {
                'timelines': [],
                'count': {"inorder":0,"order":0,"repository":0,"asset":0},
                'repository': [],
                'workorder': [],
                'months': [],
            }

        return Response(
            get_dict or {}, status.HTTP_200_OK
        )
