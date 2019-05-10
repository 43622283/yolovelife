# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from ..models import TYPE

__all__ = [
    'TYPESerializer'
]


class TYPESerializer(serializers.ModelSerializer):
    class Meta:
        model = TYPE
        fields = (
            'id', 'uuid', 'name'
        )


class TYPEDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TYPE
        fields = (
            'id', 'uuid'
        )

    def update(self, instance, validated_data):
        instance.visible()
        return super(TYPEDeleteSerializer, self).update(instance, validated_data)
