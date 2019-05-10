# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework.views import Response, status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .. import models, filter
from ..serializers import info as info_serializer
from ..permissions import info as info_permission
from deveops.api import WebTokenAuthentication

__all__ = [

]


class INFOPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 60
    page_size_query_param = 'pageSize'
    page_query_param = 'current'


class INFOINFOListAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.INFO
    serializer_class = info_serializer.INFOSerializer
    queryset = models.INFO.objects.all()
    permission_classes = [info_permission.INFOListRequiredMixin, IsAuthenticated]
    filter_class = filter.INFOFilter
    pagination_class = INFOPagination


class INFOINFOCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    serializer_class = info_serializer.INFOUpdateSerializer
    queryset = models.INFO.objects.all()
    permission_classes = [info_permission.INFOCreateRequiredMixin, IsAuthenticated]
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"

    def create(self, request, *args, **kwargs):
        return super(INFOINFOCreateAPI, self).create(request, *args, **kwargs)


class INFOINFOUpdateAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = info_serializer.INFOUpdateSerializer
    queryset = models.INFO.objects.all()
    permission_classes = [info_permission.INFOUpdateRequiredMixin, IsAuthenticated]
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"

