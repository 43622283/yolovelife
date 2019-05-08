# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
from django.conf import settings
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from deveops.api import WebTokenAuthentication
from ..permissions import role as RolePermission
from ..serializers import role as serializer
from ..serializers import user as user_serializer
from ..serializers import permission as permission_serializer
from ..filter import UserFilter, PageFilter
from .. import models
from timeline.decorator import decorator_base, decorator_api
from timeline.models import RoleHistory

__all__ = [
    'RoleUserAPI', 'RoleCreateAPI', 'RoleListAPI',
    'RolePagination'
]


class RolePagination(PageNumberPagination):
    page_size = 7
    max_page_size = 50
    page_size_query_param = 'pageSize'
    page_query_param = 'current'


class RoleListAPI(WebTokenAuthentication, generics.ListAPIView):
    serializer_class = serializer.RoleSerializer
    queryset = models.Group.objects.all().filter(name__startswith='role_')
    permission_classes = [RolePermission.RoleListRequiredMixin, IsAuthenticated]
    pagination_class = RolePagination


class RoleCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    serializer_class = serializer.RoleSerializer
    permission_classes = [RolePermission.RoleCreateRequiredMixin, IsAuthenticated]
    msg = settings.LANGUAGE.RoleCreateAPI

    @decorator_base(RoleHistory, timeline_type=settings.TIMELINE_KEY_VALUE['ROLE_CREATE'])
    def create(self, request, *args, **kwargs):
        response = super(RoleCreateAPI, self).create(request, *args, **kwargs)
        obj = models.Group.objects.get(id=response.data['id'])
        return [obj, ], self.msg.format(
            USER=request.user.full_name,
            NAME=obj.name,
        ), response


class RoleUpdateAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = serializer.RoleSerializer
    queryset = models.Group.objects.all()
    permission_classes = [RolePermission.RoleUpdateRequiredMixin, IsAuthenticated]
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'
    msg = settings.LANGUAGE.RoleUpdateAPI

    @decorator_base(RoleHistory, timeline_type=settings.TIMELINE_KEY_VALUE['ROLE_UPDATE'])
    def update(self, request, *args, **kwargs):
        response = super(RoleUpdateAPI, self).update(request, *args, **kwargs)
        obj = self.get_object()
        return [obj, ], self.msg.format(
            USER=request.user.full_name,
            NAME=obj.name,
        ), response


class RoleUserAPI(WebTokenAuthentication, generics.ListAPIView):
    serializer_class = user_serializer.UserSerializer
    permission_classes = [RolePermission.RoleListRequiredMixin, IsAuthenticated]
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'
    pagination_class = RolePagination
    filter_class = UserFilter

    def get_queryset(self):
        obj = models.Group.objects.get(
            **{self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
        )
        return obj.user_set.all()


class RoleUserAddAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = serializer.RoleUserAddSerializer
    permission_classes = [RolePermission.RoleUpdateRequiredMixin, IsAuthenticated]
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'
    msg = settings.LANGUAGE.RoleUserAddAPI

    def get_queryset(self):
        queryset = models.Group.objects.filter(
            **{self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
        )
        return queryset

    @decorator_base(RoleHistory, timeline_type=settings.TIMELINE_KEY_VALUE['ROLE_UPDATE'])
    def update(self, request, *args, **kwargs):
        response = super(RoleUserAddAPI, self).update(request, *args, **kwargs)
        obj = self.get_object()
        return [obj, ], self.msg.format(
            USER=request.user.full_name,
            NAME=obj.name,
        ), response


class RoleUserRemoveAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = serializer.RoleUserRemoveSerializer
    permission_classes = [RolePermission.RoleUpdateRequiredMixin, IsAuthenticated]
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'
    msg = settings.LANGUAGE.RoleUserRemoveAPI

    def get_queryset(self):
        queryset = models.Group.objects.filter(
            **{self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
        )
        return queryset

    @decorator_base(RoleHistory, timeline_type=settings.TIMELINE_KEY_VALUE['ROLE_UPDATE'])
    def update(self, request, *args, **kwargs):
        response = super(RoleUserRemoveAPI, self).update(request, *args, **kwargs)
        obj = self.get_object()
        return [obj, ], self.msg.format(
            USER=request.user.full_name,
            NAME=obj.name,
        ), response


class RolePageAPI(WebTokenAuthentication, generics.ListAPIView):
    serializer_class = permission_serializer.PermissionSerializer
    permission_classes = [RolePermission.RoleListRequiredMixin, IsAuthenticated]
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'
    pagination_class = RolePagination
    filter_class = PageFilter

    def get_queryset(self):
        obj = models.Group.objects.get(
            **{self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
        )
        return obj.permissions.filter(codename__startswith='deveops_page').order_by('id')


class RolePageAddAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = serializer.RolePageAddSerializer
    permission_classes = [RolePermission.RoleUpdateRequiredMixin, IsAuthenticated]
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'
    msg = settings.LANGUAGE.RolePageAddAPI

    def get_queryset(self):
        queryset = models.Group.objects.filter(
            **{self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
        )
        return queryset

    @decorator_base(RoleHistory, timeline_type=settings.TIMELINE_KEY_VALUE['ROLE_UPDATE'])
    def update(self, request, *args, **kwargs):
        response = super(RolePageAddAPI, self).update(request, *args, **kwargs)
        obj = self.get_object()
        return [obj, ], self.msg.format(
            USER=request.user.full_name,
            NAME=obj.name,
        ), response


class RolePageRemoveAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = serializer.RolePageRemoveSerializer
    permission_classes = [RolePermission.RoleUpdateRequiredMixin, IsAuthenticated]
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'
    msg = settings.LANGUAGE.RolePageRemoveAPI

    def get_queryset(self):
        queryset = models.Group.objects.filter(
            **{self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
        )
        return queryset

    @decorator_base(RoleHistory, timeline_type=settings.TIMELINE_KEY_VALUE['ROLE_UPDATE'])
    def update(self, request, *args, **kwargs):
        response = super(RolePageRemoveAPI, self).update(request, *args, **kwargs)
        obj = self.get_object()
        return [obj, ], self.msg.format(
            USER=request.user.full_name,
            NAME=obj.name,
        ), response


class RoleAPIAPI(WebTokenAuthentication, generics.ListAPIView):
    serializer_class = permission_serializer.PermissionSerializer
    permission_classes = [RolePermission.RoleListRequiredMixin, IsAuthenticated]
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'
    pagination_class = RolePagination
    filter_class = PageFilter

    def get_queryset(self):
        obj = models.Group.objects.get(
            **{self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
        )
        return obj.permissions.filter(codename__startswith='deveops_api')


class RoleAPIAddAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = serializer.RoleAPIAddSerializer
    permission_classes = [RolePermission.RoleUpdateRequiredMixin, IsAuthenticated]
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'
    msg = settings.LANGUAGE.RoleAPIAddAPI

    def get_queryset(self):
        queryset = models.Group.objects.filter(
            **{self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
        )
        return queryset

    @decorator_base(RoleHistory, timeline_type=settings.TIMELINE_KEY_VALUE['ROLE_UPDATE'])
    def update(self, request, *args, **kwargs):
        response = super(RoleAPIAddAPI, self).update(request, *args, **kwargs)
        obj = self.get_object()
        return [obj, ], self.msg.format(
            USER=request.user.full_name,
            NAME=obj.name,
        ), response


class RoleAPIRemoveAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = serializer.RoleAPIRemoveSerializer
    permission_classes = [RolePermission.RoleUpdateRequiredMixin, IsAuthenticated]
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'
    msg = settings.LANGUAGE.RoleAPIRemoveAPI

    def get_queryset(self):
        queryset = models.Group.objects.filter(
            **{self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
        )
        return queryset

    @decorator_base(RoleHistory, timeline_type=settings.TIMELINE_KEY_VALUE['ROLE_UPDATE'])
    def update(self, request, *args, **kwargs):
        response = super(RoleAPIRemoveAPI, self).update(request, *args, **kwargs)
        obj = self.get_object()
        return [obj, ], self.msg.format(
            USER=request.user.full_name,
            NAME=obj.name,
        ), response
