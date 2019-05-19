# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Time 18-1-18
# Author Yo
# Email YoLoveLife@outlook.com
from __future__ import unicode_literals
from django.db import models
from authority.models import ExtendUser
from django.conf import settings
from deveops.utils.uuid_maker import uuid_maker
from deveops.models import BaseModal

__all__ = [
    'FILE'
]


def upload_file_path(instance, filename):
    t = filename.split('.')
    return 'file/{UUID}.{FILE_TYPE}'.format(
        UUID=instance.uuid,
        FILE_TYPE=t[1],
    )

def upload_image_path(instance, filename):
    t = filename.split('.')
    return 'image/{UUID}.{IMAGE_TYPE}'.format(
        UUID=instance.uuid,
        IMAGE_TYPE=t[1],
    )


class FILE(BaseModal):
    file = models.FileField(upload_to=upload_file_path, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(ExtendUser, default=None, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        permissions = (
            ('deveops_api_list_file', u'罗列文件'),
            ('deveops_api_create_file', u'上传文件'),
            ('deveops_api_delete_file', u'删除文件'),
            ('deveops_page_file', u'文件页面'),
        )

    def url(self):
        return '{HTTP_API_DOMAIN}{URL}'.format(
            HTTP_API_DOMAIN=settings.HTTP_API_DOMAIN,
            URL=self.file.url,
        )


class IMAGE(BaseModal):
    file = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(ExtendUser, default=None, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        permissions = (
            ('deveops_api_list_image', u'罗列图片'),
            ('deveops_api_create_image', u'上传图片'),
            ('deveops_api_delete_image', u'删除图片'),
            ('deveops_page_image', u'图片页面'),
        )

    def url(self):
        return '{HTTP_API_DOMAIN}{URL}'.format(
            HTTP_API_DOMAIN=settings.HTTP_API_DOMAIN,
            URL=self.file.url,
        )