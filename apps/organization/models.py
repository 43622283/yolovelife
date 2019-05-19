# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-3
# Author Yo
# Email YoLoveLife@outlook.com
from django.db import models
from deveops.models import BaseModal

__all__ = [
    'Department', 'User'
]

class Department(BaseModal):
    father = models.ForeignKey('self', null=True, blank=True,
                               on_delete=models.SET_NULL, related_name='subdepartment')
    name = models.CharField(max_length=100, )
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (
            ('deveops_page_organization', u'组织页面'),
            ('deveops_api_list_organization', u'罗列组织'),
        )

    @property
    def organization(self):
        if self.father is None:
            return self.name
        else:
            return '{0}\{1}'.format(
                self.father.organization,
                self.name
            )

class User(BaseModal):
    username = models.CharField(max_length=30, default='')
    name = models.CharField(max_length=30, default='')
    sex = models.CharField(max_length=10, default='')
    department = models.ForeignKey(Department, null=True, blank=True,
                               on_delete=models.SET_NULL, related_name='users')

    office_phone = models.CharField(max_length=30, default='', blank=True)
    phone = models.CharField(max_length=30, default='', blank=True)
    sub_phone = models.CharField(max_length=30, default='', blank=True)
    home_phone = models.CharField(max_length=30, default='', blank=True)


    email = models.CharField(max_length=50, default='', blank=True)

    location = models.CharField(max_length=5, default='000', blank=True)
    office = models.CharField(max_length=50, default='', blank=True)

    @property
    def organization(self):
        if self.department is None:
            return '无'
        else:
            return self.department.organization