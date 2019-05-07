# !/usr/bin/env python
# Time 19-05-06
# Author Yo
# Email YoLoveLife@outlook.com
from django.contrib.auth.models import Permission
from rest_framework import serializers

__all__ = [
    'PermissionSerializer'
]


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = (
            'id', 'name', 'codename'
        )

