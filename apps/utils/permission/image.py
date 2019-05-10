# -*- coding:utf-8 -*-
from rest_framework.permissions import BasePermission
from timeline.decorator import decorator_api
from django.conf import settings

__all__ = [
    'ImageAPIRequiredMixin', 'ImageCreateRequiredMixin',
    'ImageDeleteRequiredMixin', 'ImageListRequiredMixin'
]


class ImageAPIRequiredMixin(BasePermission):
    def has_permission(self, request, view):
        perms = self.permission_required
        perm_list =list(request.user.get_all_permissions())
        if request.user.is_superuser:
            return True
        if perms in perm_list:
            return True
        else:
            return False


class ImageListRequiredMixin(ImageAPIRequiredMixin):
    permission_required = u'utils.deveops_api_list_image'


class ImageCreateRequiredMixin(ImageAPIRequiredMixin):
    permission_required = u'utils.deveops_api_create_image'


class ImageDeleteRequiredMixin(ImageAPIRequiredMixin):
    permission_required = u'utils.deveops_api_delete_image'