# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response, status
from scene.permission import location as AssetPermission
from .. import models, serializers, filter
from deveops.api import WebTokenAuthentication
from timeline.decorator import decorator_api
from django.conf import settings

__all__ = [
    'AssetPagination',
    'SceneAssetListByPageAPI',
]


class AssetPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 60
    page_size_query_param = 'pageSize'
    page_query_param = 'current'


class SceneAssetListAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.Asset
    serializer_class = serializers.AssetSerializer
    queryset = models.Asset.objects.all()
    # permission_classes = [AssetPermission.AssetListRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    filter_class = filter.AssetFilter


class SceneAssetListByPageAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.Asset
    serializer_class = serializers.AssetSerializer
    queryset = models.Asset.objects.all().order_by('-_status')
    # permission_classes = [AssetPermission.AssetListRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    pagination_class = AssetPagination
    filter_class = filter.AssetFilter

