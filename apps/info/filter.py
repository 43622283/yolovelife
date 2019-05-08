# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-6-7
# Author Yo
# Email YoLoveLife@outlook.com
import django_filters
from . import models

__all__ = [
    'DEVELOPERFilter', 'ENVIRTUALFilter', 'LOCATIONFilter', 'TYPEFilter'
]


class TYPEFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method="name_filter")

    class Meta:
        model = models.TYPE
        fields = ['name']

    @staticmethod
    def name_filter(queryset, first_name, value):
        return queryset.filter(name__contains=value)


class DEVELOPERFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method="name_filter")

    class Meta:
        model = models.DEVELOPER
        fields = ['name']

    @staticmethod
    def name_filter(queryset, first_name, value):
        return queryset.filter(name__contains=value)


class LOCATIONFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method="name_filter")

    class Meta:
        model = models.LOCATION
        fields = ['name']

    @staticmethod
    def name_filter(queryset, first_name, value):
        return queryset.filter(name__contains=value)


class ENVIRTUALFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method="name_filter")

    class Meta:
        model = models.ENVIRTUAL
        fields = ['name']

    @staticmethod
    def name_filter(queryset, first_name, value):
        return queryset.filter(name__contains=value)
