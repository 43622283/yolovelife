# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-6-7
# Author Yo
# Email YoLoveLife@outlook.com
import django_filters
from django.db.models import Q
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


class INFOFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method="name_filter")
    _type = django_filters.CharFilter(method="_type_filter")

    class Meta:
        model = models.INFO
        fields = ['name',]

    @staticmethod
    def name_filter(queryset, first_name, value):
        return queryset.filter(
                Q(name__icontains=value) | Q(detail__icontains=value)
                ).distinct()

    @staticmethod
    def _type_filter(queryset, first_name, value):
        return queryset.filter(
                _type_id=int(value)
                ).distinct()
