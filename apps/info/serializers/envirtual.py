# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from ..models import ENVIRTUAL

__all__ = [
    'ENVIRTUALSerializer'
]


class ENVIRTUALSerializer(serializers.ModelSerializer):
    class Meta:
        model = ENVIRTUAL
        fields = (
            'id', 'uuid', 'name'
        )
