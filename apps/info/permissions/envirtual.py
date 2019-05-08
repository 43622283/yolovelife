# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework.permissions import BasePermission
from django.conf import settings
__all__ = [
    'ENVIRTUALDeleteRequiredMixin', 'ENVIRTUALCreateRequiredMixin', 'ENVIRTUALAPIRequiredMixin',
    'ENVIRTUALListRequiredMixin'
]


class ENVIRTUALAPIRequiredMixin(BasePermission):
    def has_permission(self, request, view):
        perms = self.permission_required
        perm_list = list(request.user.get_all_permissions())
        if request.user.is_superuser:
            return True
        if perms in perm_list:
            return True
        else:
            return False


class ENVIRTUALListRequiredMixin(ENVIRTUALAPIRequiredMixin):
    permission_required = u'info.deveops_api_list_envirtual'


class ENVIRTUALCreateRequiredMixin(ENVIRTUALAPIRequiredMixin):
    permission_required = u'info.deveops_api_create_envirtual'


class ENVIRTUALDeleteRequiredMixin(ENVIRTUALAPIRequiredMixin):
    permission_required = u'info.deveops_api_delete_envirtual'
