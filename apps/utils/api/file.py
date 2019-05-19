# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from timeline.decorator import decorator_base
from timeline.models import FileHistory
from .. import models, serializers
from ..permissions import file as file_permission
from deveops.api import WebTokenAuthentication

__all__ = [
    'FilePagination', 'UtilsFileCreateAPI',
    'UtilsFileListAPI',
]


class FilePagination(PageNumberPagination):
    page_size = 10


class UtilsFileListAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.FILE
    serializer_class = serializers.FileSerializer
    permission_classes = [file_permission.FileListRequiredMixin, IsAuthenticated]
    pagination_class = FilePagination
    queryset = models.FILE.objects.all().order_by('-create_time')


class UtilsFileCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    module = models.FILE
    serializer_class = serializers.FileSerializer
    permission_classes = [IsAuthenticated,]#[permission.FileCreateRequiredMixin, IsAuthenticated]
    msg = settings.LANGUAGE.UtilsFileCreateAPI

    @decorator_base(FileHistory, timeline_type=settings.TIMELINE_KEY_VALUE['FILE_CREATE'])
    def create(self, request, *args, **kwargs):
        response = super(UtilsFileCreateAPI, self).create(request, *args, **kwargs)
        obj = models.FILE.objects.get(id=response.data['id'], uuid=response.data['uuid'])
        return [obj, ], self.msg.format(
            USER=request.user.full_name,
        ), response
