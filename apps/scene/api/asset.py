# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .. import models, filter
from ..serializers import asset as asset_serializer
from ..permissions import asset as asset_permission
from deveops.api import WebTokenAuthentication

__all__ = [
    'AssetPagination',
    'SceneAssetListByPageAPI',
    'SceneAssetListAPI',
]


class AssetPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 60
    page_size_query_param = 'pageSize'
    page_query_param = 'current'


class SceneAssetListAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.Asset
    serializer_class = asset_serializer.AssetSerializer
    queryset = models.Asset.objects.all()
    permission_classes = [asset_permission.AssetListRequiredMixin, IsAuthenticated]
    filter_class = filter.AssetFilter


class SceneAssetListByPageAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.Asset
    serializer_class = asset_serializer.AssetSerializer
    queryset = models.Asset.objects.all().order_by('-_status')
    permission_classes = [asset_permission.AssetListRequiredMixin, IsAuthenticated]
    pagination_class = AssetPagination
    filter_class = filter.AssetFilter

