# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-3
# Author Yo
# Email YoLoveLife@outlook.com
from datetime import datetime, date, timedelta
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import Response, status
from django_redis import get_redis_connection
from deveops.api import WebTokenAuthentication
from timeline.models import KalendarHistory
from timeline.decorator import decorator_base
from django.conf import settings
from . import models, serializers
from . import permission
from kalendar.tasks import kalendar_push

__all__ = [
]


class KalendarDaysAPI(WebTokenAuthentication, generics.ListAPIView):
    permission_classes = [permission.KalendarListRequiredMixin, IsAuthenticated]

    def list(self, request, *args, **kwargs):
        conn = get_redis_connection('kalendar')

        year, month, day = (
            request.query_params.dict()['year'],
            request.query_params.dict()['month'],
            request.query_params.dict()['day']
        )
        mid_time = date(year=int(year), month=int(month), day=int(day))
        start_time = mid_time - timedelta(days=31)
        p_time = start_time
        end_time = mid_time + timedelta(days=31)

        kalendar_dict = dict()
        while p_time < end_time:
            import json
            key = p_time.strftime('%Y-%m-%d')
            if conn.exists(key):
                kalendar_dict[key] = json.loads(conn.get(key))
            else:
                kalendar_dict[key] = []
            p_time += timedelta(days=1)

        return Response(
            kalendar_dict, status.HTTP_200_OK
        )


class KalendarListAPI(WebTokenAuthentication, generics.ListAPIView):
    permission_classes = [permission.KalendarListRequiredMixin, IsAuthenticated]

    def list(self, request, *args, **kwargs):
        kalendar_queryset = models.Kalendar.objects.filter(
            time__year=int(kwargs['year']),
            time__month=int(kwargs['month']),
            time__day=int(kwargs['day'])
        ).exclude(_visible=False)

        kalendar_serializer = serializers.KalendarSerializer(kalendar_queryset, many=True)

        return Response(
            kalendar_serializer.data, status.HTTP_200_OK
        )


class KalendarCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    serializer_class = serializers.KalendarSerializer
    permission_classes = [permission.KalendarCreateRequiredMixin, IsAuthenticated]
    msg = settings.LANGUAGE.KalendarCreateAPI

    @decorator_base(KalendarHistory, timeline_type=settings.TIMELINE_KEY_VALUE['KALENDAR_CREATE'])
    def create(self, request, *args, **kwargs):
        response = super(KalendarCreateAPI, self).create(request, *args, **kwargs)
        obj = models.Kalendar.objects.get(
            id=response.data['id'],
            uuid=response.data['uuid']
        )
        kalendar_push.delay(obj.time)
        return [obj, ], self.msg.format(
            USER=request.user.full_name,
        ), response


class KalendarUpdateAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = serializers.KalendarSerializer
    queryset = models.Kalendar.objects.all()
    permission_classes = [permission.KalendarUpdateRequiredMixin, IsAuthenticated]
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"
    msg = settings.LANGUAGE.KalendarUpdateAPI

    @decorator_base(KalendarHistory, timeline_type=settings.TIMELINE_KEY_VALUE['KALENDAR_UPDATE'])
    def update(self, request, *args, **kwargs):
        response = super(KalendarUpdateAPI, self).update(request, *args, **kwargs)
        obj = self.get_object()
        kalendar_push.delay(obj.time)
        return [obj, ], self.msg.format(
            USER=request.user.full_name,
        ), response


class KalendarDeleteAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = serializers.KalendarDeleteSerializer
    queryset = models.Kalendar.objects.all()
    permission_classes = [permission.KalendarDeleteRequiredMixin, IsAuthenticated]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'
    msg = settings.LANGUAGE.KalendarDeleteAPI

    @decorator_base(KalendarHistory, timeline_type=settings.TIMELINE_KEY_VALUE['KALENDAR_DELETE'])
    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        response = super(KalendarDeleteAPI, self).update(request, *args, **kwargs)
        kalendar_push.delay(obj.time)
        return [obj, ], self.msg.format(
            USER=request.user.full_name,
        ), response
