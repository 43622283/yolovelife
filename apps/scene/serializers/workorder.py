# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
from django.conf import settings
from rest_framework import serializers
from authority.serializers.user import UserSerializer
from .. import models
from ..serializers import classify as classify_serializer

__all__ = [

]


class WorkOrderSerializer(serializers.HyperlinkedModelSerializer):
    duty_user = UserSerializer(read_only=True)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    classify = classify_serializer.ClassifySerializer()

    class Meta:
        model = models.WorkOrder
        fields = (
            'id', 'uuid', 'create_time', 'update_time', 'serial_number', 'phone',
            'department', 'user', '_status', 'title', 'description', 'url', 'duty_user',
            'ip_address', 'mac_address', 'tags', 'src_phone', 'location', 'classify',
        )

    def create(self, validated_data):
        validated_data['duty_user'] = self.context['request'].user
        validated_data['_status'] = settings.TYPE_WORKORDER_RUN
        classify = validated_data.pop('classify')
        classify_obj = models.Classify.objects.get(uuid=classify['uuid'], name=classify['name'])
        validated_data['classify'] = classify_obj
        return super(WorkOrderSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        classify = validated_data.pop('classify')
        classify_obj = models.Classify.objects.get(uuid=classify['uuid'], name=classify['name'])
        validated_data['classify'] = classify_obj
        return super(WorkOrderSerializer, self).update(instance, validated_data)


class WorkOrderCommentSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(write_only=True)

    class Meta:
        model = models.WorkOrder
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


class WorkOrderActiveSerializer(WorkOrderSerializer):
    classify = classify_serializer.ClassifySerializer()

    class Meta:
        model = models.WorkOrder
        fields = (
            'id', 'uuid', 'serial_number', 'phone', 'department', 'user', 'title',
            'description', 'duty_user', 'tags', 'ip_address', 'mac_address', 'location'
        )

    def update(self, instance, validated_data):
        validated_data['duty_user'] = self.context['request'].user
        classify = validated_data.pop('classify')
        classify_obj = models.Classify.objects.get(uuid=classify['uuid'], name=classify['name'])
        validated_data['classify'] = classify_obj
        instance.active()
        return super(WorkOrderActiveSerializer, self).update(instance, validated_data)


class WorkOrderDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkOrder
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        instance.done()
        return super(WorkOrderDoneSerializer, self).update(instance, {})


class WorkOrderAppointSerializer(serializers.ModelSerializer):
    appoint = serializers.PrimaryKeyRelatedField(required=True, queryset=models.ExtendUser.objects.all(), write_only=True)
    class Meta:
        model = models.WorkOrder
        fields = (
            'id', 'uuid', 'appoint'
        )

    def update(self, instance, validated_data):
        appoint = validated_data.pop('appoint')
        instance.turn(appoint)
        return super(WorkOrderAppointSerializer, self).update(instance, {})
