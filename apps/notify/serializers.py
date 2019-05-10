# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-12-10
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from notify import models

__all__ = [
    'NoticeSerializer',
]


class NoticeSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(write_only=True, required=False, many=True, queryset=models.Group.objects.all())
    users = serializers.PrimaryKeyRelatedField(write_only=True, required=False, many=True, queryset=models.ExtendUser.objects.all())
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = models.Notice
        fields = (
            'id', 'uuid', 'type', 'title', 'description', 'users', 'groups',
            'create_time',
        )
        read_only_fields = (
            'id', 'uuid', 'create_time'
        )


class RemindSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(write_only=True, required=False, many=True, queryset=models.Group.objects.all())
    users = serializers.PrimaryKeyRelatedField(write_only=True, required=False, many=True, queryset=models.ExtendUser.objects.all())
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = models.Remind
        fields = (
            'id', 'uuid', 'type', 'title', 'description', 'users', 'groups',
            'create_time',
        )
        read_only_fields = (
            'id', 'uuid', 'create_time'
        )
