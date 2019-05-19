# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework.permissions import BasePermission

__all__ = [
    'NoticeCreateRequiredMixin', 'NoticeAPIRequiredMixin',
    'NoticeListRequiredMixin'
]


class NoticeAPIRequiredMixin(BasePermission):
    def has_permission(self, request, view):
        perms = self.permission_required
        perm_list = list(request.user.get_all_permissions())
        if request.user.is_superuser:
            return True
        if perms in perm_list:
            return True
        else:
            return False


class NoticeListRequiredMixin(NoticeAPIRequiredMixin):
    permission_required = u'notify.deveops_api_list_notice'


class NoticeCreateRequiredMixin(NoticeAPIRequiredMixin):
    permission_required = u'notify.deveops_api_create_notice'
