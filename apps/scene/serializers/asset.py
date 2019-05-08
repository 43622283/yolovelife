# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from scene import models

__all__ = [
    'AssetChangeUpdate2DoneSerializer', 'AssetChangeUpdate2CheckSerializer', 'AssetChangeSerializer',
    'AssetSerializer', 'AssetChangeCreate2ConfigSerializer', 'AssetChangeCreate2DoneSerializer',
    'AssetChangeCreate2InstallSerializer', 'AssetChangeScrap2CheckSerializer', 'AssetChangeScrap2DoneSerializer',
    'AssetChangeStop2CheckSerializer', 'AssetChangeStop2DoneSerializer'
]


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Asset
        fields = (
            'id', 'uuid', 'ip_address', 'mac_address', 'serial_number',
            'phone', 'department', 'user', 'location', '_status'
        )


class AssetChangeSerializer(serializers.HyperlinkedModelSerializer):
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    _connect = serializers.JSONField(source='connect', read_only=True)

    class Meta:
        model = models.AssetChange
        fields = (
            'id', 'uuid', 'ip_address', 'mac_address', 'serial_number',
            'phone', 'department', 'user', 'location', '_status', 'type', 'create_time',
            '_connect'
        )


class AssetChangeCreate2InstallSerializer(AssetChangeSerializer):
    class Meta:
        model = models.AssetChange
        fields = (
            'id', 'uuid', 'ip_address', 'mac_address', 'serial_number',
            'phone', 'department', 'user', 'location', '_status', 'type',
        )

    def create(self, validated_data):
        obj = super(AssetChangeCreate2InstallSerializer, self).create(validated_data)
        obj.self2install()
        return obj


class AssetChangeCreate2ConfigSerializer(AssetChangeSerializer):
    class Meta:
        model = models.AssetChange
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        instance.self2config()
        return super(AssetChangeCreate2ConfigSerializer, self).update(instance, validated_data)


class AssetChangeCreate2DoneSerializer(AssetChangeSerializer):
    class Meta:
        model = models.AssetChange
        fields = (
            'id', 'uuid', 'ip_address', 'mac_address', 'serial_number',
            'phone', 'department', 'user', 'location', 'type',
        )

    def update(self, instance, validated_data):
        obj = super(AssetChangeCreate2DoneSerializer, self).update(instance, validated_data)
        obj.create()
        obj.self2done()
        return obj


class AssetChangeUpdate2CheckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Asset
        fields = (
            'id', 'uuid', 'ip_address', 'mac_address', 'serial_number',
            'phone', 'department', 'user', 'location',
        )

    def update(self, instance, validated_data):
        obj = super(AssetChangeUpdate2CheckSerializer, self).update(instance, {})
        obj.update(validated_data)
        return obj


class AssetChangeUpdate2DoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AssetChange
        fields = (
            'id', 'uuid', 'ip_address', 'mac_address', 'serial_number',
            'phone', 'department', 'user', 'location',
        )

    def update(self, instance, validated_data):
        obj = super(AssetChangeUpdate2DoneSerializer, self).update(instance, validated_data)
        obj.update()
        return obj


class AssetChangeStop2CheckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Asset
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        obj = super(AssetChangeStop2CheckSerializer, self).update(instance, validated_data)
        obj.stop()
        return obj


class AssetChangeStop2DoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AssetChange
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        obj = super(AssetChangeStop2DoneSerializer, self).update(instance, validated_data)
        obj.stop()
        return obj


class AssetChangeScrap2CheckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Asset
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        obj = super(AssetChangeScrap2CheckSerializer, self).update(instance, validated_data)
        obj.scrap()
        return obj


class AssetChangeScrap2DoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AssetChange
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        obj = super(AssetChangeScrap2DoneSerializer, self).update(instance, validated_data)
        obj.scrap()
        return obj
