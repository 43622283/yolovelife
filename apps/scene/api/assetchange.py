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

]


class AssetChangePagination(PageNumberPagination):
    page_size = 5
    max_page_size = 60
    page_size_query_param = 'pageSize'
    page_query_param = 'current'


class SceneAssetChangeListByPageAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.AssetChange
    serializer_class = serializers.AssetChangeSerializer
    queryset = models.AssetChange.objects.all().order_by('_status', 'create_time')
    # permission_classes = [AssetPermission.AssetListRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    pagination_class = AssetChangePagination
    # filter_class = filter.AssetFilter


class SceneAssetChangeCreate2InstallAPI(WebTokenAuthentication, generics.CreateAPIView):
    module = models.AssetChange
    serializer_class = serializers.AssetChangeCreate2InstallSerializer
    # permission_classes = [AssetPermission.AssetCreateRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]


class SceneAssetChangeCreate2ConfigAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.AssetChange
    serializer_class = serializers.AssetChangeCreate2ConfigSerializer
    queryset = models.AssetChange.objects.all()
    permission_classes = [AllowAny, ]
    lookup_url_kwarg = 'pk'
    lookup_field = 'uuid'


class SceneAssetChangeCreate2DoneAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.AssetChange
    serializer_class = serializers.AssetChangeCreate2DoneSerializer
    permission_classes = [AllowAny, ]
    queryset = models.AssetChange.objects.all()
    lookup_url_kwarg = 'pk'
    lookup_field = 'uuid'


class SceneAssetChangeUpdate2CheckAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.Asset
    serializer_class = serializers.AssetChangeUpdate2CheckSerializer
    permission_classes = [AllowAny, ]
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
    module = models.AssetChange
    serializer_class = serializers.AssetChangeUpdate2DoneSerializer
    permission_classes = [AllowAny, ]
    queryset = models.AssetChange.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'


class SceneAssetChangeStop2CheckAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.Asset
    serializer_class = serializers.AssetChangeStop2CheckSerializer
    permission_classes = [AllowAny, ]
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
    module = models.AssetChange
    serializer_class = serializers.AssetChangeStop2DoneSerializer
    permission_classes = [AllowAny, ]
    queryset = models.AssetChange.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'


class SceneAssetChangeScrap2CheckAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.Asset
    serializer_class = serializers.AssetChangeScrap2CheckSerializer
    permission_classes = [AllowAny, ]
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
    module = models.AssetChange
    serializer_class = serializers.AssetChangeScrap2DoneSerializer
    permission_classes = [AllowAny, ]
    queryset = models.AssetChange.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
