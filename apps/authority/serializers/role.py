# !/usr/bin/env python
# Time 19-05-06
# Author Yo
# Email YoLoveLife@outlook.com
from django.contrib.auth.models import Permission
from rest_framework import serializers
from ..models import Group, ExtendUser

__all__ = [
    'RoleSerializer'
]


class RoleSerializer(serializers.ModelSerializer):
    role_name = serializers.SerializerMethodField(read_only=True)
    rolename = serializers.CharField(write_only=True)

    class Meta:
        model = Group
        fields = (
            'id', 'role_name', 'rolename'
        )

    def get_role_name(self, obj):
        return obj.name[5:]

    def create(self, validated_data):
        rolename = validated_data.pop('rolename')
        validated_data['name'] = 'role_{0}'.format(rolename)
        return super(RoleSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        role_name = validated_data.pop('rolename')
        validated_data['name'] = 'role_{0}'.format(role_name)
        return super(RoleSerializer, self).update(instance, validated_data)


class RoleUserAddSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(
        required=True, write_only=True, many=True,
        queryset=ExtendUser.objects.all()
    )

    class Meta:
        model = Group
        fields = (
            'id', 'users',
        )

    def update(self, instance, validated_data):
        users = validated_data.pop('users')
        instance.user_set.add(*users)
        return super(RoleUserAddSerializer, self).update(instance, {})


class RoleUserRemoveSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(
        required=True, write_only=True, many=True,
        queryset=ExtendUser.objects.all()
    )

    class Meta:
        model = Group
        fields = (
            'id', 'users',
        )

    def update(self, instance, validated_data):
        users = validated_data.pop('users')
        instance.user_set.remove(*users)
        return super(RoleUserRemoveSerializer, self).update(instance, {})


class RolePageAddSerializer(serializers.ModelSerializer):
    pages = serializers.PrimaryKeyRelatedField(
        required=True, write_only=True, many=True,
        queryset=Permission.objects.all()
    )

    class Meta:
        model = Group
        fields = (
            'id', 'pages',
        )

    def update(self, instance, validated_data):
        pages = validated_data.pop('pages')
        instance.permissions.add(*pages)
        return super(RolePageAddSerializer, self).update(instance, {})


class RolePageRemoveSerializer(serializers.ModelSerializer):
    pages = serializers.PrimaryKeyRelatedField(
        required=True, write_only=True, many=True,
        queryset=Permission.objects.all()
    )

    class Meta:
        model = Group
        fields = (
            'id', 'pages',
        )

    def update(self, instance, validated_data):
        pages = validated_data.pop('pages')
        instance.permissions.remove(*pages)
        return super(RolePageRemoveSerializer, self).update(instance, {})


class RoleAPIAddSerializer(serializers.ModelSerializer):
    apis = serializers.PrimaryKeyRelatedField(
        required=True, write_only=True, many=True,
        queryset=Permission.objects.all()
    )

    class Meta:
        model = Group
        fields = (
            'id', 'apis',
        )

    def update(self, instance, validated_data):
        apis = validated_data.pop('apis')
        instance.permissions.add(*apis)
        return super(RoleAPIAddSerializer, self).update(instance, {})


class RoleAPIRemoveSerializer(serializers.ModelSerializer):
    apis = serializers.PrimaryKeyRelatedField(
        required=True, write_only=True, many=True,
        queryset=Permission.objects.all()
    )

    class Meta:
        model = Group
        fields = (
            'id', 'apis',
        )

    def update(self, instance, validated_data):
        apis = validated_data.pop('apis')
        instance.permissions.remove(*apis)
        return super(RoleAPIRemoveSerializer, self).update(instance, {})
