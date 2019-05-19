# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
from django.utils.translation import ugettext_lazy as _
from django.db import models
from authority.models import ExtendUser
from django.conf import settings
from deveops.models import BaseModal
from utils.models import IMAGE

__all__ = [

]


class TYPE(BaseModal):
    name = models.CharField(max_length=100, default='无',)

    class Meta:
        permissions = (
            ('deveops_api_list_type', u'罗列信息分类'),
            ('deveops_api_create_type', u'创建信息分类'),
            ('deveops_api_delete_type', u'删除信息分类'),
        )


class DEVELOPER(BaseModal):
    name = models.CharField(max_length=100, default='无', )

    class Meta:
        permissions = (
            ('deveops_api_list_developer', u'罗列开发者'),
            ('deveops_api_create_developer', u'创建开发者'),
            ('deveops_api_delete_developer', u'删除开发者'),
        )


class LOCATION(BaseModal):
    name = models.CharField(max_length=100, default='无', )

    class Meta:
        permissions = (
            ('deveops_api_list_location', u'罗列部署地点'),
            ('deveops_api_create_location', u'创建部署地点'),
            ('deveops_api_delete_location', u'删除部署地点'),
        )


class ENVIRTUAL(BaseModal):
    name = models.CharField(max_length=100, default='无', )

    class Meta:
        permissions = (
            ('deveops_api_list_envirtual', u'罗列信息环境'),
            ('deveops_api_create_envirtual', u'创建信息环境'),
            ('deveops_api_delete_envirtual', u'删除信息环境'),
        )


class INFO(BaseModal):
    name = models.CharField(max_length=300, default='无')
    detail = models.TextField(default='无')

    main_manager = models.ForeignKey(ExtendUser, related_name='infos_A', null=True, on_delete=models.SET_NULL)
    managers = models.ManyToManyField(ExtendUser,  related_name='infos', blank=True)
    developers = models.ManyToManyField(DEVELOPER, related_name='infos', blank=True)
    operators = models.CharField(max_length=3000, default='无', null=True, blank=True)
    _type = models.ForeignKey(TYPE, related_name='infos', null=True, on_delete=models.SET_NULL)
    domain = models.TextField(default='无', null=True, blank=True)
    location = models.ForeignKey(LOCATION, related_name='infos', null=True, on_delete=models.SET_NULL)
    envirtual = models.ForeignKey(ENVIRTUAL, related_name='infos', null=True, on_delete=models.SET_NULL)
    image = models.ForeignKey(IMAGE, related_name='infos', null=True, on_delete=models.SET_NULL)

    class Meta:
        permissions = (
            ('deveops_page_info', u'信息页面'),
            ('deveops_api_list_info', u'罗列信息'),
            ('deveops_api_create_info', u'创建信息'),
            ('deveops_api_update_info', u'创建信息'),
        )
