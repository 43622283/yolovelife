# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-3
# Author Yo
# Email YoLoveLife@outlook.com
import json
from django_redis import get_redis_connection
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, status
from .. import permission as department_permission
from ..tasks import organization_department_cache
from deveops.api import WebTokenAuthentication

__all__ = [
]

class OrganizationDepartmentListAPI(WebTokenAuthentication, generics.ListAPIView):
    permission_classes = [department_permission.DepartmentListRequiredMixin, IsAuthenticated]

    def list(self, request, *args, **kwargs):
        conn = get_redis_connection('organization')
        if conn.exists('ORGANIZATION_DEPARTMENT'):
            data = conn.get('ORGANIZATION_DEPARTMENT')
            return Response(json.loads(data), status=status.HTTP_200_OK)
        else:
            organization_department_cache.delay()
            return Response(
                [], status=status.HTTP_200_OK
            )
