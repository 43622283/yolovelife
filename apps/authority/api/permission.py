# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import Permission
from authority.permission import permission as PermissionPermission
from .. import models, serializers

__all__ = [
    "PermissionListAPI", 'PermissionZDBListAPI'
]


class PermissionListAPI(generics.ListAPIView):
    module = Permission
    serializer_class = serializers.PermissionSerializer
    queryset = Permission.objects.filter(codename__istartswith="yo_")
    permission_classes = [PermissionPermission.PermissionListRequiredMixin, IsAuthenticated]


class PermissionZDBListAPI(generics.ListAPIView):
    module = Permission
    serializer_class = serializers.PermissionSerializer
    queryset = Permission.objects.filter(codename__istartswith="zdb_")
    permission_classes = [PermissionPermission.PermissionZDBListRequiredMixin, IsAuthenticated]
