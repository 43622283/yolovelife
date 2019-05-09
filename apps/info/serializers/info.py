# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
import json
from .. import models

__all__ = [
    'INFOSerializer'
]


class INFOSerializer(serializers.ModelSerializer):
    main_manager = serializers.PrimaryKeyRelatedField(required=True, queryset=models.ExtendUser.objects.all())

    managers = serializers.PrimaryKeyRelatedField(required=True, many=True, queryset=models.ExtendUser.objects.all())
    developers = serializers.PrimaryKeyRelatedField(required=True, many=True, queryset=models.DEVELOPER.objects.all())
    _type = serializers.PrimaryKeyRelatedField(required=True, queryset=models.TYPE.objects.all())
    location = serializers.PrimaryKeyRelatedField(required=True, queryset=models.LOCATION.objects.all())
    envirtual = serializers.PrimaryKeyRelatedField(required=True, queryset=models.ENVIRTUAL.objects.all())
    info_obj = serializers.JSONField(source='_info_obj')

    class Meta:
        model = models.INFO
        fields = (
            'id', 'uuid', 'name', 'detail', 'main_manager', 'managers', 'developers', 'envirtual', '_type',
            'location', 'operators', 'domain', 'image', 'info_obj'
        )
