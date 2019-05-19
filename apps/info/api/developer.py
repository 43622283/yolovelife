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
from ..serializers import developer as developer_serializer
from ..permissions import developer as developer_permission
from deveops.api import WebTokenAuthentication

__all__ = [

]


class DEVELOPERPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 60
    page_size_query_param = 'pageSize'
    page_query_param = 'current'


class INFODEVELOPERListAPI(WebTokenAuthentication, generics.ListAPIView):
    serializer_class = developer_serializer.DEVELOPERSerializer
    queryset = models.DEVELOPER.objects.filter(_visible=True)
    permission_classes = [developer_permission.DEVELOPERListRequiredMixin, IsAuthenticated]
    filter_class = filter.DEVELOPERFilter
    pagination_class = DEVELOPERPagination


class INFODEVELOPERCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    serializer_class = developer_serializer.DEVELOPERSerializer
    queryset = models.DEVELOPER.objects.all()
    permission_classes = [developer_permission.DEVELOPERCreateRequiredMixin, IsAuthenticated]
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"


class INFODEVELOPERDeleteAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = developer_serializer.DEVELOPERDeleteSerializer
    queryset = models.DEVELOPER.objects.all()
    permission_classes = [developer_permission.DEVELOPERDeleteRequiredMixin, IsAuthenticated]
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.infos.exists():
            return Response({
                'detail': '该开发者有负责的项目 无法删除'
            }, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return super(INFODEVELOPERDeleteAPI, self).update(request, *args, **kwargs)
