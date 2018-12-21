# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from zdb import models, serializers, filter
from django.conf import settings
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from deveops.api import WebTokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response, status
from zdb.permission import instance as InstancePermission
from zdb.tasks import database_single_flush

__all__ = [
    "ZDBPagination", "ZDBInstanceListAPI",
    "ZDBInstanceListByPageAPI", "ZDBInstanceCreateAPI", "ZDBInstanceDeleteAPI",
    "ZDBInstanceUpdateAPI",
]


class ZDBPagination(PageNumberPagination):
    page_size = 10


class ZDBInstanceListAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.DBInstance
    serializer_class = serializers.ZDBInstanceSerializer
    queryset = models.DBInstance.objects.all()
    # permission_classes = [InstancePermission.DBInstanceListRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny,]
    filter_class = filter.ZDBInstanceFilter


class ZDBInstanceListByPageAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.DBInstance
    serializer_class = serializers.ZDBInstanceSerializer
    queryset = models.DBInstance.objects.all()
    # permission_classes = [InstancePermission.DBInstanceListRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    pagination_class = ZDBPagination
    filter_class = filter.ZDBInstanceFilter


class ZDBInstanceFlushDatabaseAPI(WebTokenAuthentication, APIView):
    permission_classes = [AllowAny, ]

    def get_object(self):
        return models.DBInstance.objects.filter(uuid=self.kwargs['pk']).get()

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.check_status()
        return Response({
            'detail': settings.LANGUAGE.JumperStatusAPI
        }, status=status.HTTP_200_OK)


class ZDBInstanceCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    module = models.DBInstance
    serializer_class = serializers.ZDBInstanceSerializer
    queryset = models.DBInstance.objects.all()
    # permission_classes = [InstancePermission.DBInstanceCreateRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]


class ZDBInstanceUpdateAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.DBInstance
    serializer_class = serializers.ZDBInstanceSerializer
    queryset = models.DBInstance.objects.all()
    # permission_classes = [InstancePermission.DBInstanceUpdateRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    lookup_url_kwarg = 'pk'
    lookup_field = 'uuid'


class ZDBInstanceDeleteAPI(WebTokenAuthentication, generics.DestroyAPIView):
    module = models.DBInstance
    serializer_class = serializers.ZDBInstanceSerializer
    queryset = models.DBInstance.objects.all()
    # permission_classes = [InstancePermission.DBInstanceDeleteRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    lookup_url_kwarg = 'pk'
    lookup_field = 'uuid'
