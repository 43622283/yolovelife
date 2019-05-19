# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from django_redis import get_redis_connection
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, status
from rest_framework import generics
from deveops.api import WebTokenAuthentication
from .. import serializers
from ..permissions import notice as notice_permission
__all__ = [
    'NoticeCreateAPI', 'NoticeListAPI'
]


class NoticeListAPI(WebTokenAuthentication, generics.ListAPIView):
    serializer_class = serializers.NoticeSerializer
    permission_classes = [notice_permission.NoticeListRequiredMixin, IsAuthenticated]

    def list(self, request, *args, **kwargs):
        conn = get_redis_connection('notify')
        user = self.request.user

        data = conn.smembers('notify_{0}_{1}'.format(
            user.username, user.id
        ))
        return Response(
            {
                data
            }, status.HTTP_200_OK
        )


class NoticeCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    serializer_class = serializers.NoticeSerializer
    permission_classes = [notice_permission.NoticeCreateRequiredMixin, IsAuthenticated]
