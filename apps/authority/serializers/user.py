# !/usr/bin/env python
# Time 19-05-06
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from ..models import ExtendUser, Group

__all__ = [
    'UserSerializer'
]


class UserSerializer(serializers.ModelSerializer):
    group_name = serializers.StringRelatedField(source="get_group_name", read_only=True)
    email8531 = serializers.StringRelatedField(source="get_8531email", read_only=True)
    groups = serializers.PrimaryKeyRelatedField(required=False, many=True, queryset=Group.objects.all())

    class Meta:
        model = ExtendUser
        fields = (
            'id', 'uuid', 'is_active', 'phone', 'username', 'full_name', 'group_name', 'email8531', 'groups', 'email',
            'info', 'have_qrcode', 'expire',
        )
        read_only_fields = (
            'id',
        )

    def create(self, validated_data):
        obj = super(UserSerializer, self).create(validated_data=validated_data)
        obj.set_password('deveops')
        obj.save()
        return obj
