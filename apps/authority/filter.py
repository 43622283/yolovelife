# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-6-7
# Author Yo
# Email YoLoveLife@outlook.com
from django.contrib.auth.models import Permission, Group
from django.db.models import Q
import django_filters
from . import models

__all__ = [
    'UserFilter', 'GroupFilter', 'KeyFilter', 'JumperFilter'
]


class UserFilter(django_filters.FilterSet):
    phone = django_filters.CharFilter(method="phone_filter")
    is_active = django_filters.CharFilter(method="is_active_filter")
    name_username = django_filters.CharFilter(method="name_username_filter")

    class Meta:
        model = models.ExtendUser
        fields = ['phone', 'name_username', 'email', 'is_active']

    @staticmethod
    def phone_filter(queryset, first_name, value):
        return queryset.filter(phone__icontains=value)

    @staticmethod
    def name_username_filter(queryset, first_name, value):
        return queryset.filter(
            Q(first_name__icontains=value) |
            Q(full_name__icontains=value) |
            Q(username__icontains=value)
        )

    @staticmethod
    def is_active_filter(queryset, first_name, value):
        return queryset.filter(is_active=value)


class PageFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method="name_filter")

    class Meta:
        model = Permission
        fields = ['name', ]

    @staticmethod
    def name_filter(queryset, first_name, value):
        return queryset.filter(codename__startswith='deveops_page').filter(
            Q(codename__contains=value) |
            Q(name__contains=value)
        )


class APIFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method="name_filter")

    class Meta:
        model = Permission
        fields = ['name', ]

    @staticmethod
    def name_filter(queryset, first_name, value):
        return queryset.filter(codename__startswith='deveops_api').filter(
            Q(codename__contains=value) |
            Q(name__contains=value)
        )


class GroupFilter(django_filters.FilterSet):
    permission = django_filters.CharFilter(method="permission_filter")
    name = django_filters.CharFilter(method="name_filter")

    class Meta:
        model = Group
        fields = ['permission', 'name']

    @staticmethod
    def permission_filter(queryset, first_name, value):
        ps = Permission.objects.filter(codename__icontains="deveops_").filter(name__icontains=value)
        return queryset.filter(permissions__in=ps).distinct()

    @staticmethod
    def name_filter(queryset, first_name, value):
        return queryset.filter(name__icontains=value)


class KeyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method="name_filter")

    class Meta:
        model = models.Key
        fields = ['name', ]

    @staticmethod
    def name_filter(queryset, first_name, value):
        return queryset.filter(name__icontains=value)


class JumperFilter(django_filters.FilterSet):
    info = django_filters.CharFilter(method="info_filter")

    class Meta:
        model = models.Jumper
        fields = ['info',]

    @staticmethod
    def info_filter(queryset, first_name, value):
        return queryset.filter(Q(name__icontains=value) | Q(info__icontains=value))
