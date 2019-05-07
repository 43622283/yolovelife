# !/usr/bin/env python
# Time 19-05-06
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from ..models import Jumper

__all__ = [
    'JumperSerializer'
]


class JumperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jumper
        fields = (
            'id', 'uuid', 'connect_ip', 'sshport', 'name', 'info', 'status'
        )
        read_only_fields = (
            'id', 'uuid', 'status'
        )
