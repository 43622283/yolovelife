# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .. import models, filter
from ..serializers import location as location_serializer
from ..permissions import location as location_permission
from deveops.api import WebTokenAuthentication

__all__ = [

]


class LOCATIONPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 60
    page_size_query_param = 'pageSize'
    page_query_param = 'current'


class INFOLOCATIONListAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.LOCATION
    serializer_class = location_serializer.LOCATIONSerializer
    queryset = models.LOCATION.objects.all()
    permission_classes = [location_permission.LOCATIONListRequiredMixin, IsAuthenticated]
    filter_class = filter.LOCATIONFilter
    pagination_class = LOCATIONPagination


class INFOLOCATIONCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    serializer_class = location_serializer.LOCATIONSerializer
    queryset = models.LOCATION.objects.all()
    permission_classes = [location_permission.LOCATIONCreateRequiredMixin, IsAuthenticated]
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"


class INFOLOCATIONDeleteAPI(WebTokenAuthentication, generics.DestroyAPIView):
    serializer_class = location_serializer.LOCATIONSerializer
    queryset = models.LOCATION.objects.all()
    permission_classes = [location_permission.LOCATIONDeleteRequiredMixin, IsAuthenticated]
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"

