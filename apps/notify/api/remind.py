# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
import json
from notify import models, serializers
from rest_framework.views import APIView
from django_redis import get_redis_connection
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response, status
from django.conf import settings
from django.db.models import Q
from rest_framework import generics
from deveops.api import WebTokenAuthentication
__all__ = [

]


class RemindListAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.Remind
    serializer_class = serializers.RemindSerializer
    permission_classes = [AllowAny, ]

    def list(self, request, *args, **kwargs):
        conn = get_redis_connection('notify')
        user = self.request.user
        data = list()
        key = 'remind_{0}_{1}'.format(
            user.username, user.id
        )
        # conn.sadd(key, json.dumps({'id': 1, 'type': -1, 'title': '123', 'description': 123}))
        # conn.sadd(key, json.dumps({'id': 2, 'type': 1, 'title': '456', 'description': 456}))
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
    module = models.Remind
    serializer_class = serializers.RemindSerializer
    permission_classes = [AllowAny, ]
