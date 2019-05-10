# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from ..models import ENVIRTUAL

__all__ = [
    'ENVIRTUALSerializer', 'ENVIRTUALDeleteSerializer'
]


class ENVIRTUALSerializer(serializers.ModelSerializer):
    class Meta:
        model = ENVIRTUAL
        fields = (
            'id', 'uuid', 'name'
        )


class ENVIRTUALDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ENVIRTUAL
        fields = (
            'id', 'uuid'
        )

    def update(self, instance, validated_data):
        instance.visible()
        return super(ENVIRTUALDeleteSerializer, self).update(instance, validated_data)
