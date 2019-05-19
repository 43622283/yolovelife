# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-6-7
# Author Yo
# Email YoLoveLife@outlook.com
import django_filters
from django.db.models import Q
from . import models

__all__ = [

]


class UserFilter(django_filters.FilterSet):
    phone = django_filters.CharFilter(method="phone_filter")
    name = django_filters.CharFilter(method="name_filter")

    class Meta:
        model = models.User
        fields = ['phone', 'name']

    @staticmethod
    def phone_filter(queryset, first_name, value):
        return queryset.filter(
            Q(phone__contains=value) | Q(office__contains=value) |
            Q(sub_phone__contains=value) | Q(home_phone__contains=value)
        )

    @staticmethod
    def name_filter(queryset, first_name, value):
        return queryset.filter(
            Q(name__contains=value)
        )