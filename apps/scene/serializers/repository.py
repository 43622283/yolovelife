# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from authority.serializers.user import UserSerializer
from scene import models

__all__ = [
    'RepositoryMaintenanceSerializer', 'RecordSerializer', 'RepositoryExpiredSerializer', 'RepositorySerializer',
    'RepositoryDetailSerializer', 'RepositoryOkSerializer'
]


class RepositorySerializer(serializers.HyperlinkedModelSerializer):
    _comment_count = serializers.IntegerField(source='comment_count')
    _description = serializers.SerializerMethodField()
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = models.Repository
        fields = (
            'id', 'uuid', 'title', 'score', 'tags', '_comment_count', '_description', 'create_time', 'update_time',
            'status'
        )
        write_only_fields = (
            'description'
        )

    def get__description(self, obj):
        return obj.description[:305]


class RepositoryOkSerializer(RepositorySerializer):
    class Meta:
        model = models.Repository
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        instance.ok()
        return super(RepositoryOkSerializer, self).update(instance, {})


class RepositoryExpiredSerializer(RepositorySerializer):

    class Meta:
        model = models.Repository
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        instance.expired()
        return super(RepositoryExpiredSerializer, self).update(instance, {})


class RepositoryMaintenanceSerializer(RepositorySerializer):

    class Meta:
        model = models.Repository
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        instance.maintenance()
        return super(RepositoryMaintenanceSerializer, self).update(instance, {})


class RepositoryDetailSerializer(RepositorySerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.Repository
        fields = (
            'id', 'uuid', 'title', 'score', 'tags', '_comment_count', 'description', 'create_time', 'update_time',
            'user', 'status'
        )


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M', write_only=True)

    class Meta:
        model = models.Record
        fields = (
            'id', 'uuid', 'sound', 'create_time', 'phone'
        )
