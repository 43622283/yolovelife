# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response, status
from .. import models, filter
from ..serializers import classify as classify_serializer
from ..permissions import classify as classify_permission
from deveops.api import WebTokenAuthentication
from timeline.decorator import decorator_base

__all__ = [
    'ClassifyPagination', 'SceneClassifyCreateAPI', 'SceneClassifyDeleteAPI', 'SceneClassifyListAPI'
]


class ClassifyPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 60
    page_size_query_param = 'pageSize'
    page_query_param = 'current'


class SceneClassifyListAPI(WebTokenAuthentication, generics.ListAPIView):
    serializer_class = classify_serializer.ClassifySerializer
    queryset = models.Classify.objects.all()
    permission_classes = [classify_permission.ClassifyListRequiredMixin, IsAuthenticated]
    pagination_class = ClassifyPagination
    filter_class = filter.ClassifyFilter


class SceneClassifyCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    serializer_class = classify_serializer.ClassifySerializer
    permission_classes = [classify_permission.ClassifyCreateRequiredMixin, IsAuthenticated]


class SceneClassifyDeleteAPI(WebTokenAuthentication, generics.DestroyAPIView):
    serializer_class = classify_serializer.ClassifySerializer
    queryset = models.Classify.objects.all()
    permission_classes = [classify_permission.ClassifyDeleteRequiredMixin, IsAuthenticated]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'

    def delete(self, request, *args, **kwargs):
        classify = self.get_object()
        if classify.workorders.exists():
            return Response({
                'detail': '您操作的分类下有多个工单，无法删除'
            }, status=status.HTTP_406_NOT_ACCEPTABLE)

        return super(SceneClassifyDeleteAPI, self).delete(request, *args, **kwargs)
