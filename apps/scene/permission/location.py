# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework.permissions import BasePermission
from django.conf import settings
__all__ = [
    'LocationAPIRequiredMixin', 'LocationCreateRequiredMixin', 'LocationDeleteRequiredMixin',
    'LocationListRequiredMixin', 'LocationUpdateRequiredMixin'
]


class LocationAPIRequiredMixin(BasePermission):
    def has_permission(self, request, view):
        perms = self.permission_required
        perm_list = list(request.user.get_all_permissions())
        if request.user.is_superuser:
            return True
        if perms in perm_list:
            return True
        else:
            return False


class LocationListRequiredMixin(LocationAPIRequiredMixin):
    permission_required = u'scene.deveops_api_list_location'


class LocationCreateRequiredMixin(LocationAPIRequiredMixin):
    permission_required = u'scene.deveops_api_create_location'


class LocationUpdateRequiredMixin(LocationAPIRequiredMixin):
    permission_required = u'scene.deveops_api_update_location'


class LocationDeleteRequiredMixin(LocationAPIRequiredMixin):
    permission_required = u'scene.deveops_api_delete_location'

