# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
from django.contrib.auth.models import Permission
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from ..permissions import permission as PermissionPermission
from ..serializers import permission as serializer
from ..filter import PageFilter, APIFilter

__all__ = [
    "PermissionAPIListAPI", 'PermissionPageListAPI'
]


class PermissionPagination(PageNumberPagination):
    page_size = 7
    max_page_size = 50
    page_size_query_param = 'pageSize'
    page_query_param = 'current'


class PermissionAPIListAPI(generics.ListAPIView):
    module = Permission
    serializer_class = serializer.PermissionSerializer
    queryset = Permission.objects.filter(codename__istartswith="deveops_api").order_by('id')
    permission_classes = [PermissionPermission.PermissionAPIListRequiredMixin, IsAuthenticated]
    pagination_class = PermissionPagination
    filter_class = APIFilter


class PermissionPageListAPI(generics.ListAPIView):
    module = Permission
    serializer_class = serializer.PermissionSerializer
    queryset = Permission.objects.filter(codename__istartswith="deveops_page").order_by('id')
    permission_classes = [PermissionPermission.PermissionPageListRequiredMixin, IsAuthenticated]
    pagination_class = PermissionPagination
    filter_class = PageFilter
