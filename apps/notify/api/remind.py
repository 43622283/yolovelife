# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
import json
from django_redis import get_redis_connection
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, status
from rest_framework import generics
from deveops.api import WebTokenAuthentication
from .. import serializers
from ..permissions import remind as remind_permission
__all__ = [
    'RemindCreateAPI', 'RemindListAPI'
]


class RemindListAPI(WebTokenAuthentication, generics.ListAPIView):
    serializer_class = serializers.RemindSerializer
    permission_classes = [remind_permission.RemindListRequiredMixin, IsAuthenticated]

    def list(self, request, *args, **kwargs):
        conn = get_redis_connection('notify')
        user = self.request.user
        data = list()
        key = 'remind_{0}_{1}'.format(
            user.username, user.id
        )
        if conn.exists(key):
            data_set = conn.smembers(key)
            for d in data_set:
                data.append(json.loads(d))
        else:
            data = []
        conn.delete(key)
        return Response(
            {
                'remind': data
            }, status.HTTP_200_OK
        )


class RemindCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    serializer_class = serializers.RemindSerializer
    permission_classes = [remind_permission.RemindCreateRequiredMixin, IsAuthenticated]

