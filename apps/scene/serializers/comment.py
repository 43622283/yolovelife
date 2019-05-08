# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from authority.serializers.user import UserSerializer
from scene import models

__all__ = [
    'CommentSerializer', 'RepositoryCommentSerializer', 'WorkOrderCommentSerializer'
]


class WorkOrderCommentSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(write_only=True)

    class Meta:
        model = models.Repository
        fields = (
            'id', 'uuid', 'comment'
        )

    def update(self, instance, validated_data):
        obj = models.Comment.objects.create(**{
            'description': validated_data['comment'],
            'user': self.context['request'].user
        })
        instance.comments.add(obj.id)
        validated_data.pop('comment')
        return super(WorkOrderCommentSerializer, self).update(instance, validated_data)


class RepositoryCommentSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(write_only=True)

    class Meta:
        model = models.Repository
        fields = (
            'id', 'uuid', 'comment'
        )

    def update(self, instance, validated_data):
        obj = models.Comment.objects.create(**{
            'description': validated_data['comment'],
            'user': self.context['request'].user
        })
        instance.comments.add(obj.id)
        validated_data.pop('comment')
        return super(RepositoryCommentSerializer, self).update(instance, validated_data)


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = models.Comment
        fields = (
            'id', 'uuid', 'description', 'user', 'create_time'
        )