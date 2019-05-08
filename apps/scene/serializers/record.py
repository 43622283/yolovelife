# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from scene import models

__all__ = [
    'RecordSerializer'
]


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M', write_only=True)

    class Meta:
        model = models.Record
        fields = (
            'id', 'uuid', 'sound', 'create_time', 'phone'
        )
