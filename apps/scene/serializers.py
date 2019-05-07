# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from scene import models
from django.conf import settings

__all__ = [

]


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Asset
        fields = (
            'id', 'uuid', 'ip_address', 'mac_address', 'serial_number',
            'phone', 'department', 'user', 'location', '_status'
        )


class AssetChangeSerializer(serializers.HyperlinkedModelSerializer):
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    _connect = serializers.JSONField(source='connect', read_only=True)

    class Meta:
        model = models.AssetChange
        fields = (
            'id', 'uuid', 'ip_address', 'mac_address', 'serial_number',
            'phone', 'department', 'user', 'location', '_status', 'type', 'create_time',
            '_connect'
        )


class AssetChangeCreate2InstallSerializer(AssetChangeSerializer):
    class Meta:
        model = models.AssetChange
        fields = (
            'id', 'uuid', 'ip_address', 'mac_address', 'serial_number',
            'phone', 'department', 'user', 'location', '_status', 'type',
        )

    def create(self, validated_data):
        obj = super(AssetChangeCreate2InstallSerializer, self).create(validated_data)
        obj.self2install()
        return obj


class AssetChangeCreate2ConfigSerializer(AssetChangeSerializer):
    class Meta:
        model = models.AssetChange
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        instance.self2config()
        return super(AssetChangeCreate2ConfigSerializer, self).update(instance, validated_data)


class AssetChangeCreate2DoneSerializer(AssetChangeSerializer):
    class Meta:
        model = models.AssetChange
        fields = (
            'id', 'uuid', 'ip_address', 'mac_address', 'serial_number',
            'phone', 'department', 'user', 'location', 'type',
        )

    def update(self, instance, validated_data):
        obj = super(AssetChangeCreate2DoneSerializer, self).update(instance, validated_data)
        obj.create()
        obj.self2done()
        return obj


class AssetChangeUpdate2CheckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Asset
        fields = (
            'id', 'uuid', 'ip_address', 'mac_address', 'serial_number',
            'phone', 'department', 'user', 'location',
        )

    def update(self, instance, validated_data):
        obj = super(AssetChangeUpdate2CheckSerializer, self).update(instance, {})
        obj.update(validated_data)
        return obj


class AssetChangeUpdate2DoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AssetChange
        fields = (
            'id', 'uuid', 'ip_address', 'mac_address', 'serial_number',
            'phone', 'department', 'user', 'location',
        )

    def update(self, instance, validated_data):
        obj = super(AssetChangeUpdate2DoneSerializer, self).update(instance, validated_data)
        obj.update()
        return obj


class AssetChangeStop2CheckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Asset
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        obj = super(AssetChangeStop2CheckSerializer, self).update(instance, validated_data)
        obj.stop()
        return obj


class AssetChangeStop2DoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AssetChange
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        obj = super(AssetChangeStop2DoneSerializer, self).update(instance, validated_data)
        obj.stop()
        return obj


class AssetChangeScrap2CheckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Asset
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        obj = super(AssetChangeScrap2CheckSerializer, self).update(instance, validated_data)
        obj.scrap()
        return obj


class AssetChangeScrap2DoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AssetChange
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        obj = super(AssetChangeScrap2DoneSerializer, self).update(instance, validated_data)
        obj.scrap()
        return obj


class WorkOrderDutyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ExtendUser
        fields = (
            'id', 'full_name', 'email', 'phone', 'info',
        )


class WorkOrderSerializer(serializers.HyperlinkedModelSerializer):
    duty_user = WorkOrderDutyUserSerializer(read_only=True)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = models.WorkOrder
        fields = (
            'id', 'uuid', 'create_time', 'update_time', 'serial_number', 'phone',
            'department', 'user', '_status', 'title', 'description', 'sound', 'duty_user',
            'ip_address', 'mac_address', 'tags', 'src_phone', 'location'
        )

    def create(self, validated_data):
        validated_data['duty_user'] = self.context['request'].user
        validated_data['_status'] = settings.TYPE_WORKORDER_RUN
        return super(WorkOrderSerializer, self).create(validated_data)


class WorkOrderCommentSerializer(WorkOrderSerializer):
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


class WorkOrderActiveSerializer(WorkOrderSerializer):

    class Meta:
        model = models.WorkOrder
        fields = (
            'id', 'uuid', 'serial_number', 'phone', 'department', 'user', 'title',
            'description', 'duty_user', 'tags', 'ip_address', 'mac_address', 'location'
        )

    def update(self, instance, validated_data):
        validated_data['duty_user'] = self.context['request'].user
        instance.active()
        return super(WorkOrderActiveSerializer, self).update(instance, validated_data)


class WorkOrderDoneSerializer(WorkOrderSerializer):
    class Meta:
        model = models.WorkOrder
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        instance.done()
        return super(WorkOrderDoneSerializer, self).update(instance, {})


class WorkOrderAppointSerializer(WorkOrderSerializer):
    appoint_id = serializers.IntegerField(required=True, write_only=True)

    class Meta:
        model = models.WorkOrder
        fields = (
            'id', 'uuid', 'appoint_id'
        )

    def update(self, instance, validated_data):
        print('serialier')
        obj = models.ExtendUser.objects.get(id=validated_data['appoint_id'])
        instance.turn(obj)
        return super(WorkOrderAppointSerializer, self).update(instance, {})


class RepositorySerializer(serializers.HyperlinkedModelSerializer):
    _comment_count = serializers.IntegerField(source='comment_count')
    _description = serializers.SerializerMethodField()
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = models.Repository
        fields = (
            'id', 'uuid', 'title', 'score', 'tags', '_comment_count', '_description', 'create_time', 'update_time',
            'status'
        )
        write_only_fields = (
            'description'
        )

    def get__description(self, obj):
        return obj.description[:305]


class RepositoryOkSerializer(RepositorySerializer):
    class Meta:
        model = models.Repository
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        instance.ok()
        return super(RepositoryOkSerializer, self).update(instance, {})


class RepositoryExpiredSerializer(RepositorySerializer):

    class Meta:
        model = models.Repository
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        instance.expired()
        return super(RepositoryExpiredSerializer, self).update(instance, {})


class RepositoryMaintenanceSerializer(RepositorySerializer):

    class Meta:
        model = models.Repository
        fields = (
            'id', 'uuid',
        )

    def update(self, instance, validated_data):
        instance.maintenance()
        return super(RepositoryMaintenanceSerializer, self).update(instance, {})


class RepositoryCommentSerializer(RepositorySerializer):
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
    user = WorkOrderDutyUserSerializer(read_only=True)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = models.Comment
        fields = (
            'id', 'uuid', 'description', 'user', 'create_time'
        )


class RepositoryDetailSerializer(RepositorySerializer):
    user = WorkOrderDutyUserSerializer(read_only=True)

    class Meta:
        model = models.Repository
        fields = (
            'id', 'uuid', 'title', 'score', 'tags', '_comment_count', 'description', 'create_time', 'update_time',
            'user', 'status'
        )


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M', write_only=True)

    class Meta:
        model = models.Record
        fields = (
            'id', 'uuid', 'sound', 'create_time', 'phone'
        )
