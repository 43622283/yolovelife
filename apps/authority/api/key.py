# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, status
from rest_framework.pagination import PageNumberPagination
from deveops.api import WebTokenAuthentication
from ..permissions import key as KeyPermission
from ..serializers import key as serializer
from .. import models, filter
from timeline.decorator import decorator_base
from timeline.models import KeyHistory

__all__ = [
    "KeyListAPI", "KeyCreateAPI", "KeyUpdateAPI",
    "KeyDeleteAPI", 'KeyPagination'
]


class KeyPagination(PageNumberPagination):
    page_size = 10


class KeyListAPI(WebTokenAuthentication, generics.ListAPIView):
    serializer_class = serializer.KeySerializer
    queryset = models.Key.objects.filter(_visible=True)
    permission_classes = [KeyPermission.KeyListRequiredMixin, IsAuthenticated]
    pagination_class = KeyPagination
    filter_class = filter.KeyFilter


class KeyCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    serializer_class = serializer.KeySerializer
    permission_classes = [KeyPermission.KeyCreateRequiredMixin, IsAuthenticated]
    msg = settings.LANGUAGE.KeyCreateAPI

    @decorator_base(KeyHistory, timeline_type=settings.TIMELINE_KEY_VALUE['KEY_CREATE'])
    def create(self, request, *args, **kwargs):
        response = super(KeyCreateAPI, self).create(request, *args, **kwargs)
        obj = models.Key.objects.get(id=response.data['id'], uuid=response.data['uuid'])
        return [obj, ], self.msg.format(
            USER=request.user.full_name,
            NAME=response.data['name'],
            UUID=response.data['uuid'],
        ), response


class KeyUpdateAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = serializer.KeySerializer
    queryset = models.Key.objects.all()
    permission_classes = [KeyPermission.KeyUpdateRequiredMixin, IsAuthenticated]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'
    msg = settings.LANGUAGE.KeyUpdateAPI

    @decorator_base(KeyHistory, timeline_type=settings.TIMELINE_KEY_VALUE['KEY_UPDATE'])
    def update(self, request, *args, **kwargs):
        response = super(KeyUpdateAPI, self).update(request, *args, **kwargs)
        key = self.get_object()
        return [key, ], self.msg.format(
            USER=request.user.full_name,
            NAME=key.name,
            UUID=key.uuid
        ), response


class KeyDeleteAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = serializer.KeyDeleteSerializer
    queryset = models.Key.objects.all()
    permission_classes = [KeyPermission.KeyDeleteRequiredMixin, IsAuthenticated]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'
    msg = settings.LANGUAGE.KeyDeleteAPI

    @decorator_base(KeyHistory, timeline_type=settings.TIMELINE_KEY_VALUE['KEY_DELETE'])
    def update(self, request, *args, **kwargs):
        response = super(KeyDeleteAPI, self).update(request, *args, **kwargs)
        key = self.get_object()
        return [key, ], self.msg.format(
            USER=request.user.full_name,
            NAME=key.name,
            UUID=key.uuid
        ), response
