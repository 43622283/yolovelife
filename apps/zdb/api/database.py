# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from zdb import models,serializers,filter
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from deveops.api import WebTokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response, status
from zdb.permission import instance as InstancePermission

__all__ = [
    "ZDBPagination", "ZDBInstanceListAPI",
    "ZDBInstanceListByPageAPI", "ZDBInstanceCreateAPI", "ZDBInstanceDeleteAPI",
    "ZDBInstanceUpdateAPI",
]


class ZDBPagination(PageNumberPagination):
    page_size = 10


class ZDBDatabaseListAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.DBDatabase
    serializer_class = serializers.ZDBDatabaseSerializer
    queryset = models.DBDatabase.objects.all()
    # permission_classes = [InstancePermission.DBInstanceListRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    filter_class = filter.ZDBDatabaseFilter


class ZDBDatabaseListByPageAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.DBDatabase
    serializer_class = serializers.ZDBDatabaseSerializer
    queryset = models.DBDatabase.objects.all()
    # permission_classes = [InstancePermission.DBInstanceListRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    pagination_class = ZDBPagination
    filter_class = filter.ZDBDatabaseFilter
