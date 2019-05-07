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
from scene.permission import location as RepositoryPermission
from .. import models, serializers, filter
from deveops.api import WebTokenAuthentication
from timeline.decorator import decorator_api
from django.conf import settings

__all__ = [

]


class RepositoryPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 60
    page_size_query_param = 'pageSize'
    page_query_param = 'current'


class SceneRepositoryListByPageAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.Repository
    serializer_class = serializers.RepositorySerializer
    queryset = models.Repository.objects.all().order_by('-score', '-status', '-update_time')
    # permission_classes = [RepositoryPermission.RepositoryListRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    pagination_class = RepositoryPagination
    filter_class = filter.RepositoryFilter


class SceneRepositoryCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    module = models.Repository
    serializer_class = serializers.RepositorySerializer
    # permission_classes = [RepositoryPermission.RepositoryCreateRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    # msg = settings.LANGUAGE.SceneRepositoryCreateAPI

    # @decorator_api(timeline_type=settings.TIMELINE_KEY_VALUE['HOST_CREATE'])
    # def create(self, request, *args, **kwargs):
    #     if self.qrcode_check(request):
    #         response = super(ManagerHostCreateAPI, self).create(request, *args, **kwargs)
    #         return self.msg.format(
    #             USER=request.user.full_name,
    #             HOSTNAME=response.data['hostname'],
    #             CONNECT_IP=response.data['connect_ip'],
    #             UUID=response.data['uuid'],
    #         ), response
    #     else:
    #         return '', self.qrcode_response


class SceneRepositoryUpdateAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.Repository
    serializer_class = serializers.RepositorySerializer
    queryset = models.Repository.objects.all()
    # permission_classes = [RepositoryPermission.RepositoryUpdateRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"
    # msg = settings.LANGUAGE.SceneRepositoryUpdateAPI

    # @decorator_api(timeline_type=settings.TIMELINE_KEY_VALUE['HOST_UPDATE'])
    # def update(self, request, *args, **kwargs):
    #     if self.qrcode_check(request):
    #         response = super(SceneRepositoryUpdateAPI, self).update(request, *args, **kwargs)
    #         host = self.get_object()
    #         return self.msg.format(
    #             USER=request.user.full_name,
    #             HOSTNAME=host.hostname,
    #             CONNECT_IP=host.connect_ip,
    #             UUID=host.uuid,
    #         ), response
    #     else:
    #         return '', self.qrcode_response


class SceneRepositoryStarsAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.Repository
    serializer_class = serializers.RepositorySerializer
    queryset = models.Repository.objects.all()
    # permission_classes = [RepositoryPermission.RepositoryUpdateRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"
    # msg = settings.LANGUAGE.SceneRepositoryUpdateAPI

    # @decorator_api(timeline_type=settings.TIMELINE_KEY_VALUE['HOST_UPDATE'])
    # def update(self, request, *args, **kwargs):
    #     if self.qrcode_check(request):
    #         response = super(SceneRepositoryUpdateAPI, self).update(request, *args, **kwargs)
    #         host = self.get_object()
    #         return self.msg.format(
    #             USER=request.user.full_name,
    #             HOSTNAME=host.hostname,
    #             CONNECT_IP=host.connect_ip,
    #             UUID=host.uuid,
    #         ), response
    #     else:
    #         return '', self.qrcode_response


class SceneRepositoryCommentAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.Repository
    serializer_class = serializers.RepositoryCommentSerializer
    queryset = models.Repository.objects.all()
    # permission_classes = [RepositoryPermission.RepositoryDeleteRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'


class SceneRepositoryBeOkAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.Repository
    serializer_class = serializers.RepositoryOkSerializer
    queryset = models.Repository.objects.all()
    # permission_classes = [RepositoryPermission.RepositoryDeleteRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'


class SceneRepositoryBeExpiredAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.Repository
    serializer_class = serializers.RepositoryExpiredSerializer
    queryset = models.Repository.objects.all()
    # permission_classes = [RepositoryPermission.RepositoryDeleteRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'


class SceneRepositoryBeMaintenanceAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.Repository
    serializer_class = serializers.RepositoryMaintenanceSerializer
    queryset = models.Repository.objects.all()
    # permission_classes = [RepositoryPermission.RepositoryDeleteRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'


class SceneRepositoryDeleteAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.Repository
    serializer_class = serializers.RepositorySerializer
    queryset = models.Repository.objects.all()
    # permission_classes = [RepositoryPermission.RepositoryDeleteRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'
    # msg = settings.LANGUAGE.SceneRepositoryDeleteAPI

    # @decorator_api(timeline_type=settings.TIMELINE_KEY_VALUE['HOST_DELETE'])
    # def update(self, request, *args, **kwargs):
    #     if self.qrcode_check(request):
    #         host = self.get_object()
    #         response = super(SceneRepositoryDeleteAPI, self).update(request, *args, **kwargs)
    #         return self.msg.format(
    #             USER=request.user.full_name,
    #             HOSTNAME=host.hostname,
    #             CONNECT_IP=host.connect_ip,
    #             UUID=host.uuid,
    #         ), response
    #     else:
    #         return '', self.qrcode_response


class SceneRepositoryDetailAPI(WebTokenAuthentication, generics.ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = models.Repository.objects.all()
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"

    def list(self, request, *args, **kwargs):
        obj = self.get_object()

        repository_serializer = serializers.RepositoryDetailSerializer(obj)

        comment_serializer = serializers.CommentSerializer(obj.comments.order_by('create_time'), many=True)

        return Response(
            {
                'repository': repository_serializer.data,
                'comments': comment_serializer.data,
            }, status.HTTP_200_OK
        )
