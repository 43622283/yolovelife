# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework.permissions import BasePermission

__all__ = [
    'KalendarDeleteRequiredMixin', 'KalendarCreateRequiredMixin', 'KalendarAPIRequiredMixin',
    'KalendarListRequiredMixin'
]


class KalendarAPIRequiredMixin(BasePermission):
    def has_permission(self, request, view):
        perms = self.permission_required
        perm_list = list(request.user.get_all_permissions())
        if request.user.is_superuser:
            return True
        if perms in perm_list:
            return True
        else:
            return False


class KalendarListRequiredMixin(KalendarAPIRequiredMixin):
    permission_required = u'kalendar.deveops_api_list_kalendar'


class KalendarCreateRequiredMixin(KalendarAPIRequiredMixin):
    permission_required = u'kalendar.deveops_api_create_kalendar'


class KalendarUpdateRequiredMixin(KalendarAPIRequiredMixin):
    permission_required = u'kalendar.deveops_api_update_kalendar'


class KalendarDeleteRequiredMixin(KalendarAPIRequiredMixin):
    permission_required = u'kalendar.deveops_api_delete_kalendar'
