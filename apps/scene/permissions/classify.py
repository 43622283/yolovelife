# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework.permissions import BasePermission

__all__ = [
    'ClassifyAPIRequiredMixin', 'ClassifyCreateRequiredMixin', 'ClassifyListRequiredMixin',
]


class ClassifyAPIRequiredMixin(BasePermission):
    def has_permission(self, request, view):
        perms = self.permission_required
        perm_list = list(request.user.get_all_permissions())
        if request.user.is_superuser:
            return True
        if perms in perm_list:
            return True
        else:
            return False


class ClassifyListRequiredMixin(ClassifyAPIRequiredMixin):
    permission_required = u'scene.deveops_api_list_classify'


class ClassifyCreateRequiredMixin(ClassifyAPIRequiredMixin):
    permission_required = u'scene.deveops_api_create_classify'


class ClassifyDeleteRequiredMixin(ClassifyAPIRequiredMixin):
    permission_required = u'scene.deveops_api_delete_classify'
