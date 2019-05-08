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
from .. import models, filter
from ..serializers import repository as repository_serializer
from ..serializers import comment as comment_serializer
from ..permissions import repository as repository_permission
from deveops.api import WebTokenAuthentication
from timeline.decorator import decorator_base

__all__ = [

]


class RepositoryPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 60
    page_size_query_param = 'pageSize'
    page_query_param = 'current'


class SceneRepositoryListByPageAPI(WebTokenAuthentication, generics.ListAPIView):
    serializer_class = repository_serializer.RepositorySerializer
    queryset = models.Repository.objects.all().order_by('-score', '-status', '-update_time')
    permission_classes = [repository_permission.RepositoryListRequiredMixin, IsAuthenticated]
    pagination_class = RepositoryPagination
    filter_class = filter.RepositoryFilter


class SceneRepositoryCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    serializer_class = repository_serializer.RepositorySerializer
    permission_classes = [repository_permission.RepositoryCreateRequiredMixin, IsAuthenticated]
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
    serializer_class = repository_serializer.RepositorySerializer
    queryset = models.Repository.objects.all()
    permission_classes = [repository_permission.RepositoryUpdateRequiredMixin, IsAuthenticated]
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
    serializer_class = repository_serializer.RepositorySerializer
    queryset = models.Repository.objects.all()
    permission_classes = [repository_permission.RepositoryUpdateRequiredMixin, IsAuthenticated]
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
    serializer_class = comment_serializer.RepositoryCommentSerializer
    queryset = models.Repository.objects.all()
    permission_classes = [repository_permission.RepositoryDeleteRequiredMixin, IsAuthenticated]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'


class SceneRepositoryBeOkAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = repository_serializer.RepositoryOkSerializer
    queryset = models.Repository.objects.all()
    permission_classes = [repository_permission.RepositoryUpdateRequiredMixin, IsAuthenticated]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'


class SceneRepositoryBeExpiredAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = repository_serializer.RepositoryExpiredSerializer
    queryset = models.Repository.objects.all()
    permission_classes = [repository_permission.RepositoryUpdateRequiredMixin, IsAuthenticated]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'


class SceneRepositoryBeMaintenanceAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = repository_serializer.RepositoryMaintenanceSerializer
    queryset = models.Repository.objects.all()
    permission_classes = [repository_permission.RepositoryUpdateRequiredMixin, IsAuthenticated]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'


class SceneRepositoryDeleteAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = repository_serializer.RepositorySerializer
    queryset = models.Repository.objects.all()
    permission_classes = [repository_permission.RepositoryDeleteRequiredMixin, IsAuthenticated]
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
    permission_classes = [repository_permission.RepositoryListRequiredMixin, IsAuthenticated]
    queryset = models.Repository.objects.all()
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"

    def list(self, request, *args, **kwargs):
        obj = self.get_object()

        repo_serializer = repository_serializer.RepositoryDetailSerializer(obj)

        com_serializer = comment_serializer.CommentSerializer(obj.comments.order_by('create_time'), many=True)

        return Response(
            {
                'repository': repo_serializer.data,
                'comments': com_serializer.data,
            }, status.HTTP_200_OK
        )
