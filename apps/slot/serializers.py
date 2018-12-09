# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-12-10
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from slot import models

__all__ = [
    'SlotSerializer',
]


class SlotSerializer(serializers.HyperlinkedModelSerializer):
    group_name = serializers.CharField(source="group.name", read_only=True)

    class Meta:
        model = models.Slot
        fields = (
            'id', 'uuid', 'type', 'info', 'time', 'group_name'
        )
        read_only_fields = (
            'id', 'uuid',
        )
