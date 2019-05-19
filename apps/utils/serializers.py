from . import models
from rest_framework import serializers

__all__ = [
    'FileSerializer',
]


class FileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.full_name', read_only=True)

    class Meta:
        model = models.FILE
        fields = (
            'id', 'uuid', 'file', 'user',
        )
        read_only_fields = (
            'id', 'uuid', 'create_time',
        )

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(FileSerializer, self).create(validated_data)


class ImageSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.full_name', read_only=True)

    class Meta:
        model = models.IMAGE
        fields = (
            'id', 'uuid', 'file', 'user',
        )
        read_only_fields = (
            'id', 'uuid', 'create_time',
        )

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(ImageSerializer, self).create(validated_data)