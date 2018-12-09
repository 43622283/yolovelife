# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from slot import models, serializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response, status
from django.conf import settings
from django.db.models import Q
from rest_framework import generics
from deveops.api import WebTokenAuthentication
__all__ = [
    'SlotPagination', 'SlotListByPageAPI',
]


class SlotPagination(PageNumberPagination):
    page_size = 10


class SlotListByPageAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.Slot
    serializer_class = serializers.SlotSerializer
    permission_classes = [AllowAny, ]
    pagination_class = SlotPagination

    def get_queryset(self):
        user = self.request.user
        pmn_groups = user.groups

        groups = models.Group.objects.filter(
            Q(users=user) or Q(pmn_groups__in=pmn_groups)
        )

        queryset = models.Slot.objects.filter(group_id__in=groups)
        return queryset
