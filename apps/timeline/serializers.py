# -*- coding:utf-8 -*-
from timeline import models
from rest_framework import serializers

__all__ = [
    "HistorySerializer", 'SceneHistorySerializer',
]


class HistorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.History
        fields = (
            'id', 'uuid', 'msg', 'type', 'time',
        )
        read_only_fields = (
            'id', 'uuid',
        )


class SceneHistorySerializer(HistorySerializer):
    time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = models.SceneHistory
        fields = (
            'id', 'uuid', 'msg', 'type', 'time',
        )
