# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-3
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .. import permission as user_permission
from .. import models
from ..filter import UserFilter
from ..serializers import user as user_serializer
from deveops.api import WebTokenAuthentication

__all__ = [
]

class UserPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 60
    page_size_query_param = 'pageSize'
    page_query_param = 'current'


class OrganizationUserListAPI(WebTokenAuthentication, generics.ListAPIView):
    permission_classes = [user_permission.UserListRequiredMixin, IsAuthenticated]
    serializer_class = user_serializer.UserSerializer
    pagination_class = UserPagination
    lookup_url_kwarg = 'pk'
    lookup_field = 'uuid'
    filter_class = UserFilter

    def get_queryset(self):
        if str(self.kwargs[self.lookup_url_kwarg]) == '00000000-0000-0000-0000-000000000000':
            obj = models.Department.objects.get(
                father__isnull=True
            )
        else:
            obj = models.Department.objects.get(
                **{self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
            )

        if obj.father is None:
            return models.User.objects.all()
        else:
            return obj.users.all()
