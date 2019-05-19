# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FormParser, MultiPartParser
from django.conf import settings
from timeline.decorator import decorator_base
from timeline.models import ImageHistory
from .. import models, serializers
from ..permissions import image as image_permission
from deveops.api import WebTokenAuthentication

__all__ = [
    'ImagePagination', 'UtilsImageCreateAPI',
    'UtilsImageListAPI',
]


class ImagePagination(PageNumberPagination):
    page_size = 10


class UtilsImageListAPI(WebTokenAuthentication, generics.ListAPIView):
    serializer_class = serializers.ImageSerializer
    permission_classes = [image_permission.ImageListRequiredMixin, IsAuthenticated]
    pagination_class = ImagePagination
    queryset = models.IMAGE.objects.all().order_by('-create_time')


class UtilsImageCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    serializer_class = serializers.ImageSerializer
    permission_classes = [IsAuthenticated, ]#[permission.ImageCreateRequiredMixin, IsAuthenticated]
    msg = settings.LANGUAGE.UtilsImageCreateAPI
    parser_classes = (FormParser, MultiPartParser)

    @decorator_base(ImageHistory, timeline_type=settings.TIMELINE_KEY_VALUE['IMAGE_CREATE'])
    def create(self, request, *args, **kwargs):
        response = super(UtilsImageCreateAPI, self).create(request, *args, **kwargs)
        obj = models.IMAGE.objects.get(id=response.data['id'], uuid=response.data['uuid'])
        return [obj, ], self.msg.format(
            USER=request.user.full_name,
        ), response
