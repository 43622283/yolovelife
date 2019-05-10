# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from .. import models
from ..serializers import developer, envirtual, location, type
from authority.serializers import user


__all__ = [
    'INFOSerializer'
]


class INFOSerializer(serializers.ModelSerializer):
    main_manager = user.UserSerializer(read_only=True)
    managers = user.UserSerializer(read_only=True, many=True)
    developers = developer.DEVELOPERSerializer(read_only=True, many=True)
    _type = type.TYPESerializer(read_only=True)
    location = location.LOCATIONSerializer(read_only=True)
    envirtual = envirtual.ENVIRTUALSerializer(read_only=True)

    class Meta:
        model = models.INFO
        fields = (
            'id', 'uuid', 'name', 'detail', 'main_manager', 'managers', 'developers', 'envirtual', '_type',
            'location', 'operators', 'domain', 'image',
        )


class INFOUpdateSerializer(serializers.ModelSerializer):
    # main_manager = serializers.PrimaryKeyRelatedField(required=True, queryset=models.ExtendUser.objects.all())
    # managers = serializers.PrimaryKeyRelatedField(required=True, many=True, queryset=models.ExtendUser.objects.all())
    # developers = serializers.PrimaryKeyRelatedField(required=True, many=True, queryset=models.DEVELOPER.objects.all())
    # _type = serializers.PrimaryKeyRelatedField(required=True, queryset=models.TYPE.objects.all())
    # location = serializers.PrimaryKeyRelatedField(required=True, queryset=models.LOCATION.objects.all())
    # envirtual = serializers.PrimaryKeyRelatedField(required=True, queryset=models.ENVIRTUAL.objects.all())

    class Meta:
        model = models.INFO
        fields = (
            'id', 'uuid', 'name', 'detail', 'image',
        )

'''
'main_manager', 'managers', 'developers', 'envirtual', '_type',
            'location', 'operators', 'domain', 
'''