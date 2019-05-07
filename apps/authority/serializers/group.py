# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
from django.contrib.auth.models import Permission
from rest_framework import serializers
from ..models import Group

__all__ = [
    'GroupSerializer'
]


class GroupSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(required=False, many=True, queryset=Permission.objects.all())

    class Meta:
        model = Group
        fields = (
            'id', 'name', 'permissions'
        )
