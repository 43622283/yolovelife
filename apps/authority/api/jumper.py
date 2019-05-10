# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.views import Response, status
from rest_framework.pagination import PageNumberPagination
from deveops.api import WebTokenAuthentication
from ..permissions import jumper as JumperPermission
from ..serializers import jumper as serializer
from .. import models, filter
from timeline.models import JumperHistory
from timeline.decorator import decorator_base


__all__ = [
    "JumperListAPI", "JumperCreateAPI", "JumperUpdateAPI",
    "JumperDeleteAPI", "JumperPagination",
]


class JumperPagination(PageNumberPagination):
    page_size = 10


class JumperListAPI(WebTokenAuthentication, generics.ListAPIView):
    serializer_class = serializer.JumperSerializer
    queryset = models.Jumper.objects.filter(_visible=True)
    permission_classes = [JumperPermission.JumperListRequiredMixin, IsAuthenticated]
    filter_class = filter.JumperFilter
    pagination_class = JumperPagination


class JumperStatusAPI(WebTokenAuthentication, APIView):
    permission_classes = [JumperPermission.JumperStatusRequiredMixin, IsAuthenticated]

    def get_object(self):
        return models.Jumper.objects.filter(uuid=self.kwargs['pk']).get()

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.check_status()
        return Response({
            'detail': settings.LANGUAGE.JumperStatusAPI
        }, status=status.HTTP_200_OK)


class JumperCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    serializer_class = serializer.JumperSerializer
    permission_classes = [JumperPermission.JumperCreateRequiredMixin, IsAuthenticated]
    msg = settings.LANGUAGE.JumperCreateAPI

    @decorator_base(JumperHistory, timeline_type=settings.TIMELINE_KEY_VALUE['FILE_CREATE'])
    def create(self, request, *args, **kwargs):
        response = super(JumperCreateAPI, self).create(request, *args, **kwargs)
        obj = self.get_object()
        return [obj, ], self.msg.format(
            USER=request.user.full_name,
            NAME=response.data['name'],
            UUID=response.data['uuid'],
            CONNECT_IP=response.data['connect_ip']
        ), response


class JumperUpdateAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = serializer.JumperSerializer
    queryset = models.Jumper.objects.all()
    permission_classes = [JumperPermission.JumperUpdateRequiredMixin, IsAuthenticated]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'
    msg = settings.LANGUAGE.JumperUpdateAPI

    @decorator_base(JumperHistory, timeline_type=settings.TIMELINE_KEY_VALUE['FILE_UPDATE'])
    def update(self, request, *args, **kwargs):
        response = super(JumperUpdateAPI, self).update(request, *args, **kwargs)
        jumper = self.get_object()
        return [jumper, ], self.msg.format(
            USER=request.user.full_name,
            NAME=jumper.name,
            UUID=jumper.uuid,
            CONNECT_IP=jumper.connect_ip
        ), response


class JumperDeleteAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = serializer.JumperDeleteSerializer
    queryset = models.Jumper.objects.all()
    permission_classes = [JumperPermission.JumperDeleteRequiredMixin, IsAuthenticated]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'
    msg = settings.LANGUAGE.JumperDeleteAPI

    @decorator_base(JumperHistory, timeline_type=settings.TIMELINE_KEY_VALUE['JUMPER_DELETE'])
    def update(self, request, *args, **kwargs):
        response = super(JumperDeleteAPI, self).update(request, *args, **kwargs)
        jumper = self.get_object()
        return [jumper, ], self.msg.format(
            USER=request.user.full_name,
            NAME=jumper.name,
            UUID=jumper.uuid,
            CONNECT_IP=jumper.connect_ip
        ), response
