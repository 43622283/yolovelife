# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
from django.conf import settings
from rest_framework import serializers
from .. import models

__all__ = [

]


class WorkOrderHistorySerializer(serializers.HyperlinkedModelSerializer):
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = models.WorkOrderHistory
        fields = (
            'id', 'uuid', 'msg', 'type', 'create_time',
        )
