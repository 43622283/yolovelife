# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
from django.contrib.auth.models import Permission
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..permissions import permission as PermissionPermission
from ..serializers import permission as serializer

__all__ = [
    "PermissionAPIListAPI", 'PermissionPageListAPI'
]


class PermissionAPIListAPI(generics.ListAPIView):
    module = Permission
    serializer_class = serializer.PermissionSerializer
    queryset = Permission.objects.filter(codename__istartswith="deveops_api")
    permission_classes = [PermissionPermission.PermissionAPIListRequiredMixin, IsAuthenticated]


class PermissionPageListAPI(generics.ListAPIView):
    module = Permission
    serializer_class = serializer.PermissionSerializer
    queryset = Permission.objects.filter(codename__istartswith="deveops_page")
    permission_classes = [PermissionPermission.PermissionPageListRequiredMixin, IsAuthenticated]
