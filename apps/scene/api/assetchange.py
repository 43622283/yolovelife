# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response, status
from .. import models
from ..serializers import asset as asset_serializer
from ..permissions import asset as asset_permission
from deveops.api import WebTokenAuthentication
from timeline.decorator import decorator_base
from timeline.models import AssetHistory
from django.conf import settings

__all__ = [

]


class AssetChangePagination(PageNumberPagination):
    page_size = 5
    max_page_size = 60
    page_size_query_param = 'pageSize'
    page_query_param = 'current'


class SceneAssetChangeListAPI(WebTokenAuthentication, generics.ListAPIView):
    serializer_class = asset_serializer.AssetChangeSerializer
    queryset = models.AssetChange.objects.all().order_by('_status', 'create_time')
    permission_classes = [asset_permission.AssetListRequiredMixin, IsAuthenticated]
    pagination_class = AssetChangePagination
    # filter_class = filter.AssetFilter


class SceneAssetChangeCreate2InstallAPI(WebTokenAuthentication, generics.CreateAPIView):
    serializer_class = asset_serializer.AssetChangeCreate2InstallSerializer
    permission_classes = [asset_permission.AssetCreateRequiredMixin, IsAuthenticated]

    @decorator_base(AssetHistory, timeline_type=settings.TIMELINE_KEY_VALUE['ASSET_CREATE'])
    def create(self, request, *args, **kwargs):
        response = super(SceneAssetChangeCreate2InstallAPI, self).create(request, *args, **kwargs)
        obj = models.AssetChange.objects.get(id=response.data['id'], uuid=response.data['uuid'])
        return [obj, ], self.msg.format(
            USER=request.user.full_name,
            NAME=response.data['name'],
        ), response


class SceneAssetChangeCreate2ConfigAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = asset_serializer.AssetChangeCreate2ConfigSerializer
    queryset = models.AssetChange.objects.all()
    permission_classes = [asset_permission.AssetCreateRequiredMixin, IsAuthenticated]
    lookup_url_kwarg = 'pk'
    lookup_field = 'uuid'


class SceneAssetChangeCreate2DoneAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = asset_serializer.AssetChangeCreate2DoneSerializer
    permission_classes = [asset_permission.AssetCreateRequiredMixin, IsAuthenticated]
    queryset = models.AssetChange.objects.all()
    lookup_url_kwarg = 'pk'
    lookup_field = 'uuid'


class SceneAssetChangeUpdate2CheckAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = asset_serializer.AssetChangeUpdate2CheckSerializer
    permission_classes = [asset_permission.AssetUpdateRequiredMixin, IsAuthenticated]
    queryset = models.Asset.objects.all()
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj._status < settings.STATUS_ASSET_DONE:
            return Response(
                {'detail': '当前资产是无法操作状态 请将原有的资产操作流程完毕'}, status=status.HTTP_406_NOT_ACCEPTABLE
            )
        return super(SceneAssetChangeUpdate2CheckAPI, self).update(
            request, *args, **kwargs
        )


class SceneAssetChangeUpdate2DoneAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = asset_serializer.AssetChangeUpdate2DoneSerializer
    permission_classes = [asset_permission.AssetUpdateRequiredMixin, IsAuthenticated]
    queryset = models.AssetChange.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'


class SceneAssetChangeStop2CheckAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = asset_serializer.AssetChangeStop2CheckSerializer
    permission_classes = [asset_permission.AssetStopRequiredMixin, IsAuthenticated]
    queryset = models.Asset.objects.all()
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj._status < settings.STATUS_ASSET_DONE:
            return Response(
                {'detail': '当前资产是无法操作状态 请将原有的资产操作流程完毕'}, status=status.HTTP_406_NOT_ACCEPTABLE
            )
        return super(SceneAssetChangeStop2CheckAPI, self).update(
            request, *args, **kwargs
        )


class SceneAssetChangeStop2DoneAPI(WebTokenAuthentication, generics.UpdateAPIView):
    permission_classes = [asset_permission.AssetStopRequiredMixin, IsAuthenticated]
    queryset = models.AssetChange.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'


class SceneAssetChangeScrap2CheckAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = asset_serializer.AssetChangeScrap2CheckSerializer
    permission_classes = [asset_permission.AssetScrapRequiredMixin, IsAuthenticated]
    queryset = models.Asset.objects.all()
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj._status < settings.STATUS_ASSET_DONE:
            return Response(
                {'detail': '当前资产是无法操作状态 请将原有的资产操作流程完毕'}, status=status.HTTP_406_NOT_ACCEPTABLE
            )
        return super(SceneAssetChangeScrap2CheckAPI, self).update(
            request, *args, **kwargs
        )


class SceneAssetChangeScrap2DoneAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = asset_serializer.AssetChangeScrap2DoneSerializer
    permission_classes = [asset_permission.AssetScrapRequiredMixin, IsAuthenticated]
    queryset = models.AssetChange.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
