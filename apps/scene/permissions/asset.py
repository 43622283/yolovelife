# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework.permissions import BasePermission
from django.conf import settings
__all__ = [
    'AssetAPIRequiredMixin', 'AssetCreateRequiredMixin',
    'AssetListRequiredMixin', 'AssetUpdateRequiredMixin',
    'AssetScrapRequiredMixin', 'AssetStopRequiredMixin'
]


class AssetAPIRequiredMixin(BasePermission):
    def has_permission(self, request, view):
        perms = self.permission_required
        perm_list = list(request.user.get_all_permissions())
        if request.user.is_superuser:
            return True
        if perms in perm_list:
            return True
        else:
            return False


class AssetListRequiredMixin(AssetAPIRequiredMixin):
    permission_required = u'scene.deveops_api_list_asset'


class AssetCreateRequiredMixin(AssetAPIRequiredMixin):
    permission_required = u'scene.deveops_api_create_asset'


class AssetUpdateRequiredMixin(AssetAPIRequiredMixin):
    permission_required = u'scene.deveops_api_update_asset'


class AssetStopRequiredMixin(AssetAPIRequiredMixin):
    permission_required = u'scene.deveops_api_stop_asset'


class AssetScrapRequiredMixin(AssetAPIRequiredMixin):
    permission_required = u'scene.deveops_api_scrap_asset'
