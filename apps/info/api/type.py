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
from ..serializers import type as type_serializer
from ..permissions import type as type_permission
from deveops.api import WebTokenAuthentication

__all__ = [

]


class TYPEPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 60
    page_size_query_param = 'pageSize'
    page_query_param = 'current'


class INFOTYPEListAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.TYPE
    serializer_class = type_serializer.TYPESerializer
    queryset = models.TYPE.objects.filter(_visible=True)
    permission_classes = [type_permission.TYPEListRequiredMixin, IsAuthenticated]
    filter_class = filter.TYPEFilter
    pagination_class = TYPEPagination


class INFOTYPECreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    serializer_class = type_serializer.TYPESerializer
    queryset = models.TYPE.objects.all()
    permission_classes = [type_permission.TYPECreateRequiredMixin, IsAuthenticated]
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"


class INFOTYPEDeleteAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = type_serializer.TYPEDeleteSerializer
    queryset = models.TYPE.objects.all()
    permission_classes = [type_permission.TYPEDeleteRequiredMixin, IsAuthenticated]
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.infos.exists():
            return Response({
                'detail': '该类型有挂钩的项目 无法删除'
            }, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return super(INFOTYPEDeleteAPI, self).update(request, *args, **kwargs)