# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-3
# Author Yo
# Email YoLoveLife@outlook.com
from datetime import datetime, date, timedelta
from django_redis import get_redis_connection
from rest_framework import generics
from rest_framework.views import APIView
from . import models, serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import Response, status
from rest_framework.views import APIView
from django_redis import get_redis_connection
from deveops.api import WebTokenAuthentication
from django.conf import settings
from manager.models import Group
from kalendar.tasks import kalendar_push

__all__ = [
]


class KalendarDaysAPI(WebTokenAuthentication, generics.ListAPIView):
    # permission_classes = [AssetPermission.AssetListRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]

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
    # permission_classes = [AssetPermission.AssetListRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]

    def list(self, request, *args, **kwargs):
        kalendar_queryset = models.Kalendar.objects.filter(
            time__year=int(kwargs['year']),
            time__month=int(kwargs['month']),
            time__day=int(kwargs['day'])
        )

        kalendar_serializer = serializers.KalendarSerializer(kalendar_queryset, many=True)

        return Response(
            kalendar_serializer.data, status.HTTP_200_OK
        )


class KalendarCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    module = models.Kalendar
    serializer_class = serializers.KalendarSerializer
    # permission_classes = [RepositoryPermission.RepositoryCreateRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    # msg = settings.LANGUAGE.SceneRepositoryCreateAPI

    # @decorator_api(timeline_type=settings.TIMELINE_KEY_VALUE['HOST_CREATE'])
    # def create(self, request, *args, **kwargs):
    #     if self.qrcode_check(request):
    #         response = super(ManagerHostCreateAPI, self).create(request, *args, **kwargs)
    #         return self.msg.format(
    #             USER=request.user.full_name,
    #             HOSTNAME=response.data['hostname'],
    #             CONNECT_IP=response.data['connect_ip'],
    #             UUID=response.data['uuid'],
    #         ), response
    #     else:
    #         return '', self.qrcode_response

    def create(self, request, *args, **kwargs):
        response = super(KalendarCreateAPI, self).create(request, *args, **kwargs)
        obj = models.Kalendar.objects.get(
            id=response.data['id'],
            uuid=response.data['uuid']
        )
        kalendar_push.delay(obj.time)
        return response


class KalendarUpdateAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.Kalendar
    serializer_class = serializers.KalendarSerializer
    queryset = models.Kalendar.objects.all()
    # permission_classes = [RepositoryPermission.RepositoryUpdateRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"
    # msg = settings.LANGUAGE.SceneRepositoryUpdateAPI

    # @decorator_api(timeline_type=settings.TIMELINE_KEY_VALUE['HOST_UPDATE'])
    # def update(self, request, *args, **kwargs):
    #     if self.qrcode_check(request):
    #         response = super(SceneRepositoryUpdateAPI, self).update(request, *args, **kwargs)
    #         host = self.get_object()
    #         return self.msg.format(
    #             USER=request.user.full_name,
    #             HOSTNAME=host.hostname,
    #             CONNECT_IP=host.connect_ip,
    #             UUID=host.uuid,
    #         ), response
    #     else:
    #         return '', self.qrcode_response
    def update(self, request, *args, **kwargs):
        response = super(KalendarUpdateAPI, self).update(request, *args, **kwargs)
        obj = self.get_object()
        kalendar_push.delay(obj.time)
        return response


class KalendarDeleteAPI(WebTokenAuthentication, generics.DestroyAPIView):
    module = models.Kalendar
    serializer_class = serializers.KalendarSerializer
    queryset = models.Kalendar.objects.all()
    # permission_classes = [RepositoryPermission.RepositoryDeleteRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'
    # msg = settings.LANGUAGE.SceneRepositoryDeleteAPI

    # @decorator_api(timeline_type=settings.TIMELINE_KEY_VALUE['HOST_DELETE'])
    # def update(self, request, *args, **kwargs):
    #     if self.qrcode_check(request):
    #         host = self.get_object()
    #         response = super(SceneRepositoryDeleteAPI, self).update(request, *args, **kwargs)
    #         return self.msg.format(
    #             USER=request.user.full_name,
    #             HOSTNAME=host.hostname,
    #             CONNECT_IP=host.connect_ip,
    #             UUID=host.uuid,
    #         ), response
    #     else:
    #         return '', self.qrcode_response

    def delete(self, request, *args, **kwargs):
        time = self.get_object().time
        response = super(KalendarDeleteAPI, self).delete(request, *args, **kwargs)
        kalendar_push.delay(time)
        return response
