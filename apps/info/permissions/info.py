# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework.permissions import BasePermission

__all__ = [
    'INFOUpdateRequiredMixin', 'INFOCreateRequiredMixin', 'INFOAPIRequiredMixin', 'INFOListRequiredMixin'
]


class INFOAPIRequiredMixin(BasePermission):
    def has_permission(self, request, view):
        perms = self.permission_required
        perm_list = list(request.user.get_all_permissions())
        if request.user.is_superuser:
            return True
        if perms in perm_list:
            return True
        else:
            return False


class INFOListRequiredMixin(INFOAPIRequiredMixin):
    permission_required = u'info.deveops_api_list_info'


class INFOCreateRequiredMixin(INFOAPIRequiredMixin):
    permission_required = u'info.deveops_api_create_info'


class INFOUpdateRequiredMixin(INFOAPIRequiredMixin):
    permission_required = u'info.deveops_api_update_info'
