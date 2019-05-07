# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response, status
from rest_framework.parsers import FileUploadParser, MultiPartParser
from scene.permission import location as AssetPermission
from .. import models, serializers, filter
from deveops.api import WebTokenAuthentication
from django.conf import settings
from deveops.utils import aes
import datetime
__all__ = [

]

SALT = 'workorder:'


class SceneRecordCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    module = models.Record
    serializer_class = serializers.RecordSerializer
    permission_classes = [AllowAny, ]
    parser_classes = (MultiPartParser, FileUploadParser,)

    def create(self, request, *args, **kwargs):
        data = request.data
        if data['secret'] != str(aes.encrypt(data['create_time'] + SALT),
                                 encoding="utf8"):
            return Response(
                {'detail': u'校验错误'}, status=status.HTTP_200_OK)
        else:
            request.data.pop('secret')
        return super(SceneRecordCreateAPI, self).create(request, *args, **kwargs)
