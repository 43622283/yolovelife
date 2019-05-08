# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-6-7
# Author Yo
# Email YoLoveLife@outlook.com
import django_filters
from django.db.models import Q
from scene import models
import datetime

__all__ = [

]


class AssetFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(method="user_filter")
    ip_address = django_filters.CharFilter(method="ip_filter")
    phone = django_filters.CharFilter(method="phone_filter")
    department_location = django_filters.CharFilter(method="department_location_filter")
    user_phone = django_filters.CharFilter(method="user_phone_filter")
    user_phone_split = django_filters.CharFilter(method="user_phone_split_filter")
    status = django_filters.CharFilter(method="status_filter")

    class Meta:
        model = models.Asset
        fields = ['user', 'ip_address', 'phone', 'department', 'status']

    @staticmethod
    def user_filter(queryset, first_name, value):
        return queryset.filter(user__contains=value)

    @staticmethod
    def ip_filter(queryset, first_name, value):
        return queryset.filter(ip_address__contains=value)

    @staticmethod
    def phone_filter(queryset, first_name, value):
        return queryset.filter(phone__contains=value)

    @staticmethod
    def department_location_filter(queryset, first_name, value):
        return queryset.filter(Q(department__contains=value) | Q(location__contains=value))

    @staticmethod
    def user_phone_filter(queryset, first_name, value):
        return queryset.filter(Q(user__contains=value) | Q(phone__contains=value))

    @staticmethod
    def user_phone_split_filter(queryset, first_name, value):
        return queryset.filter(Q(user__contains=value) | Q(phone__contains=value))[:20]

    @staticmethod
    def status_filter(queryset, first_name, value):
        return queryset.filter(_status=value)


class WorkOrderFilter(django_filters.FilterSet):
    duty_user = django_filters.CharFilter(method="duty_user_filter")
    title = django_filters.CharFilter(method="title_filter")
    status = django_filters.CharFilter(method="status_filter")
    is_create = django_filters.BooleanFilter(method="is_create_filter")
    own = django_filters.CharFilter(method="own_filter")

    class Meta:
        model = models.WorkOrder
        fields = ['duty_user', 'title', 'is_create', 'status']

    @staticmethod
    def duty_user_filter(queryset, first_name, value):
        return queryset.filter(duty_user__full_name__contains=value)

    @staticmethod
    def title_filter(queryset, first_name, value):
        return queryset.filter(title__contains=value)

    @staticmethod
    def status_filter(queryset, first_name, value):
        return queryset.filter(_status=value)

    @staticmethod
    def is_create_filter(queryset, first_name, value):
        if value:
            return queryset.filter(Q(src_phone="") | Q(src_phone__isnull=True))
        else:
            return queryset.filter(~Q(src_phone=""))

    @staticmethod
    def own_filter(queryset, first_name, value):
        obj = models.ExtendUser.objects.get(username=value)
        return queryset.filter(duty_user=obj)


class RepositoryFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(method="title_filter")

    class Meta:
        model = models.Repository
        fields = ['title']

    @staticmethod
    def title_filter(queryset, first_name, value):
        return queryset.filter(title__contains=value)


class CommentFilter(django_filters.FilterSet):
    uuid = django_filters.CharFilter(method="uuid_filter")

    class Meta:
        model = models.Comment
        fields = ['uuid']

    @staticmethod
    def uuid_filter(queryset, first_name, value):
        return queryset.filter(repository__uuid=value)


class ClassifyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method="name_filter")

    class Meta:
        model = models.Classify
        fields = ['name']

    @staticmethod
    def name_filter(queryset, first_name, value):
        return queryset.filter(name__contains=value)
