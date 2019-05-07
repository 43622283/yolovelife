# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-3
# Author Yo
# Email YoLoveLife@outlook.com
from . import models, serializers
from rest_framework import serializers

__all__ = [

]


STATUS_TYPE = {
    3: 'processing',
    2: 'default',
    1: 'warning',
    -1: 'success',
    -2: 'error',
}


class KalendarSerializer(serializers.HyperlinkedModelSerializer):
    time = serializers.DateTimeField(format='%Y-%m-%d', required=False)
    type = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Kalendar
        fields = (
            'id', 'uuid', 'time', 'status', 'title', 'description', 'type'
        )

    def get_type(self, obj):
        return STATUS_TYPE[obj.status]

