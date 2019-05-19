# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from ..models import Classify

__all__ = [
    'ClassifySerializer'
]


class ClassifySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Classify
        fields = (
            'id', 'uuid', 'name'
        )


class ClassifyDeleteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Classify
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        instance.visible()
        return super(ClassifyDeleteSerializer, self).update(instance, validated_data)