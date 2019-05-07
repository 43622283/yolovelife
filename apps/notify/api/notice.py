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


class NoticeListAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.Notice
    serializer_class = serializers.NoticeSerializer
    permission_classes = [AllowAny, ]

    def list(self, request, *args, **kwargs):
        conn = get_redis_connection('notify')
        user = self.request.user

        data = conn.smembers('notify_{0}_{1}'.format(
            # user.username, user.id
            1, 1
        ))
        # conn.sadd('notify_1_1', json.dumps({'id':'1', 'title':'123'}))
        # conn.sadd('notify_1_1', json.dumps({'id': '2', 'title': '456'}))
        # conn.sadd('notify_1_1', json.dumps({'id': '3', 'title': '789'}))

        return Response(
            {
                data
            }, status.HTTP_200_OK
        )


class NoticeCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    module = models.Notice
    serializer_class = serializers.NoticeSerializer
    permission_classes = [AllowAny, ]
