# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .. import models, filter
from ..serializers import envirtual as envirtual_serializer
from ..permissions import envirtual as envirtual_permission
from deveops.api import WebTokenAuthentication

__all__ = [

]


class ENVIRTUALPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 60
    page_size_query_param = 'pageSize'
    page_query_param = 'current'


class INFOENVIRTUALListAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.ENVIRTUAL
    serializer_class = envirtual_serializer.ENVIRTUALSerializer
    queryset = models.ENVIRTUAL.objects.all()
    permission_classes = [envirtual_permission.ENVIRTUALListRequiredMixin, IsAuthenticated]
    filter_class = filter.ENVIRTUALFilter
    pagination_class = ENVIRTUALPagination


class INFOENVIRTUALCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    serializer_class = envirtual_serializer.ENVIRTUALSerializer
    queryset = models.ENVIRTUAL.objects.all()
    permission_classes = [envirtual_permission.ENVIRTUALCreateRequiredMixin, IsAuthenticated]
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"


class INFOENVIRTUALDeleteAPI(WebTokenAuthentication, generics.DestroyAPIView):
    serializer_class = envirtual_serializer.ENVIRTUALSerializer
    queryset = models.ENVIRTUAL.objects.all()
    permission_classes = [envirtual_permission.ENVIRTUALDeleteRequiredMixin, IsAuthenticated]
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"

