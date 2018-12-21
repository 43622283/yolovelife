# -*- coding:utf-8 -*-
from rest_framework import serializers
from zdb import models
__all__ = [
    "ZDBInstanceSerializer",
]


class ZDBInstanceSerializer(serializers.HyperlinkedModelSerializer):
    passwd = serializers.CharField(required=False, allow_null=True, source='password', write_only=True)
    _status = serializers.CharField(source="status", read_only=True)

    class Meta:
        model = models.DBInstance
        fields = (
            'id', 'uuid', 'name', 'connect_address', 'port', 'is_master', '_status', 'user', 'passwd', 'create_time',
        )
        read_only_fields = (
            'id', 'uuid', '_status', 'create_time'
        )


class ZDBDatabaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DBDatabase
        fields = (
            'id', 'uuid', 'name',
        )