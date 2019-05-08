# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, status
from .. import models, filter
from ..serializers import comment as comment_serializer
from ..permissions import comment as comment_permission
from deveops.api import WebTokenAuthentication
from timeline.decorator import decorator_base

__all__ = [

]


class SceneCommentListAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.Comment
    serializer_class = comment_serializer.CommentSerializer
    queryset = models.Comment.objects.all()
    permission_classes = [comment_permission.CommentListRequiredMixin, IsAuthenticated]
    filter_class = filter.CommentFilter


class SceneCommentCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    module = models.Comment
    serializer_class = comment_serializer.CommentSerializer
    permission_classes = [comment_permission.CommentCreateRequiredMixin, IsAuthenticated]
    # msg = settings.LANGUAGE.SceneCommentCreateAPI

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


# class SceneCommentUpdateAPI(WebTokenAuthentication, generics.UpdateAPIView):
#     module = models.Comment
#     serializer_class = serializers.CommentSerializer
#     queryset = models.Comment.objects.all()
    # permission_classes = [CommentPermission.CommentUpdateRequiredMixin, IsAuthenticated]
    # permission_classes = [AllowAny, ]
    # lookup_field = "uuid"
    # lookup_url_kwarg = "pk"
    # msg = settings.LANGUAGE.SceneCommentUpdateAPI

    # @decorator_api(timeline_type=settings.TIMELINE_KEY_VALUE['HOST_UPDATE'])
    # def update(self, request, *args, **kwargs):
    #     if self.qrcode_check(request):
    #         response = super(SceneCommentUpdateAPI, self).update(request, *args, **kwargs)
    #         host = self.get_object()
    #         return self.msg.format(
    #             USER=request.user.full_name,
    #             HOSTNAME=host.hostname,
    #             CONNECT_IP=host.connect_ip,
    #             UUID=host.uuid,
    #         ), response
    #     else:
    #         return '', self.qrcode_response


# class SceneCommentStarsAPI(WebTokenAuthentication, generics.UpdateAPIView):
#     module = models.Comment
#     serializer_class = serializers.CommentSerializer
#     queryset = models.Comment.objects.all()
    # permission_classes = [CommentPermission.CommentUpdateRequiredMixin, IsAuthenticated]
    # permission_classes = [AllowAny, ]
    # lookup_field = "uuid"
    # lookup_url_kwarg = "pk"
    # msg = settings.LANGUAGE.SceneCommentUpdateAPI

    # @decorator_api(timeline_type=settings.TIMELINE_KEY_VALUE['HOST_UPDATE'])
    # def update(self, request, *args, **kwargs):
    #     if self.qrcode_check(request):
    #         response = super(SceneCommentUpdateAPI, self).update(request, *args, **kwargs)
    #         host = self.get_object()
    #         return self.msg.format(
    #             USER=request.user.full_name,
    #             HOSTNAME=host.hostname,
    #             CONNECT_IP=host.connect_ip,
    #             UUID=host.uuid,
    #         ), response
    #     else:
    #         return '', self.qrcode_response


class SceneCommentDeleteAPI(WebTokenAuthentication, generics.DestroyAPIView):
    module = models.Comment
    serializer_class = comment_serializer.CommentSerializer
    queryset = models.Comment.objects.all()
    permission_classes = [comment_permission.CommentDeleteRequiredMixin, IsAuthenticated]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'
    # msg = settings.LANGUAGE.SceneCommentDeleteAPI

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user.id != request.user.id:
            return Response({'detail': u'您无法删除非自己评论的内容'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return super(SceneCommentDeleteAPI, self).delete(request, *args, **kwargs)
    # @decorator_api(timeline_type=settings.TIMELINE_KEY_VALUE['HOST_DELETE'])
    # def update(self, request, *args, **kwargs):
    #     if self.qrcode_check(request):
    #         host = self.get_object()
    #         response = super(SceneCommentDeleteAPI, self).update(request, *args, **kwargs)
    #         return self.msg.format(
    #             USER=request.user.full_name,
    #             HOSTNAME=host.hostname,
    #             CONNECT_IP=host.connect_ip,
    #             UUID=host.uuid,
    #         ), response
    #     else:
    #         return '', self.qrcode_response

