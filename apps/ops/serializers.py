# -*- coding: utf-8 -*-
import yaml
from ops import models
from rest_framework import serializers

__all__ = [
    "MetaSerializer", "MissionNeedFileSerializer",
    "MissionSerializer",
]


class MetaSerializer(serializers.ModelSerializer):
    hosts = serializers.PrimaryKeyRelatedField(required=False, many=True,
                                               queryset=models.Host.objects.all(),
                                               allow_null=True)
    need_files = serializers.ListField(source="file_list", read_only=True)
    _tasks = serializers.CharField(required=True, source="tasks")
    group = serializers.PrimaryKeyRelatedField(queryset=models.Group.objects.all())
    group_name = serializers.CharField(source="group.name", read_only=True)

    class Meta:
        model = models.META
        fields = (
            'id', 'uuid', 'hosts', '_tasks', 'group', 'group_name', 'info', 'need_files',
            'level', 'facts'
        )
        read_only_fields = (
            'id', 'uuid', 'group_name'
        )


class MissionNeedFileSerializer(serializers.ModelSerializer):
    filelist = serializers.ListField(source='file_list', read_only=True)

    class Meta:
        model = models.Mission
        fields = (
            'filelist',
        )


class MissionSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=models.Group.objects.all())
    metas = serializers.PrimaryKeyRelatedField(many=True, queryset=models.META.objects.all())
    group_name = serializers.CharField(source="group.name", read_only=True)
    counts = serializers.IntegerField(source="count", read_only=True)
    playbook = serializers.CharField(source="_playbook", read_only=True)

    class Meta:
        model = models.Mission
        fields = (
            'id', 'uuid', 'group', 'metas', 'info', 'need_validate', 'group_name', 'counts', 'playbook'
        )
        read_only_fields = (
            'id', 'uuid', 'group_name', 'counts', 'playbook'
        )


class QuickGitMissionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True, required=True)
    src_git = serializers.CharField(write_only=True, required=True)
    src_branch = serializers.CharField(write_only=True, required=True)
    src_path = serializers.CharField(write_only=True, required=True)
    dest_path = serializers.CharField(write_only=True, required=True)

    hosts = serializers.PrimaryKeyRelatedField(required=True, many=True, queryset=models.Host.objects.all(), allow_null=True)
    group = serializers.PrimaryKeyRelatedField(queryset=models.Group.objects.all(), required=True)
    need_validate = serializers.BooleanField(default=False)

    class Meta:
        model = models.Mission
        fields = (
            'name', 'src_git', 'src_branch', 'src_path', 'dest_path', 'hosts', 'group', 'need_validate'
        )

    def create(self, validated_data):
        # Check out
        checkout_task_obj = {
            'tasks': [
                {
                    'name': 'Checkout',
                    'git': 'repo={0} dest={1}/code version={2}'.format(
                        validated_data['src_git'],
                        "{{BASE}}",
                        validated_data['src_branch'],
                    ),
                }
            ]
        }

        checkout_meta = models.META.objects.create(
            group=validated_data['group'],
            info=validated_data['name']+'检出代码Checkout',
            _tasks=checkout_task_obj,
            level=1,
            facts=False,
        )

        # Sync
        sync_task_obj = {
            'tasks': [
                {
                    'name': 'Sync',
                    'synchronize': 'src={0}/code{1} dest={2} compress=yes use_ssh_args=yes'.format(
                        "{{BASE}}",
                        validated_data['src_path'],
                        validated_data['dest_path'],
                    ),
                }
            ]
        }

        sync_meta = models.META.objects.create(
            group=validated_data['group'],
            info=validated_data['name'] + '检出代码Sync',
            _tasks=sync_task_obj,
            level=2,
            facts=False,
        )

        sync_meta.hosts.set(validated_data['hosts'])

        # Mission
        mission = models.Mission.objects.create(
            group=validated_data['group'],
            info=validated_data['name'],
            need_validate=validated_data['need_validate'],
        )
        mission.metas.set([checkout_meta, sync_meta])
        return mission


class QuickFileMissionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True, required=True)
    filename = serializers.CharField(write_only=True, required=True)
    dest_file = serializers.CharField(write_only=True, required=True)

    hosts = serializers.PrimaryKeyRelatedField(required=True, many=True, queryset=models.Host.objects.all(), allow_null=True)
    group = serializers.PrimaryKeyRelatedField(queryset=models.Group.objects.all(), required=True)
    need_validate = serializers.BooleanField(default=False)

    class Meta:
        model = models.Mission
        fields = (
            'name', 'filename', 'dest_file', 'hosts', 'group', 'need_validate'
        )

    def create(self, validated_data):
        # Copy
        copy_task_obj = {
            'tasks': [
                {
                    'name': 'Copy',
                    'copy': 'src=<file>{FILENAME} dest={DEST}'.format(
                            FILENAME='{{'+validated_data['filename']+'}}',
                            DEST=validated_data['dest_file'],
                    ),
                }
            ]
        }
        copy_meta = models.META.objects.create(
            group=validated_data['group'],
            info=validated_data['name'] + '拷贝文件Copy',
            _tasks=copy_task_obj,
            level=1,
        )

        copy_meta.hosts.set(validated_data['hosts'])

        # Mission
        mission = models.Mission.objects.create(
            group=validated_data['group'],
            info=validated_data['name'],
            need_validate=validated_data['need_validate'],
        )
        mission.metas.set([copy_meta, ])
        return mission


class QuickSerializer(serializers.Serializer):
    metatype = serializers.CharField(required=True,)
    data = serializers.JSONField(required=True,)

    class Meta:
        model = models.Quick
        fields = (
            'id', 'uuid', 'data', 'metatype'
        )

    # TODO: Maybe create wrong?
    def create(self, validated_data):
        data = validated_data.pop('data')
        if validated_data['metatype'] == 'git':
            ser = QuickGitMissionSerializer(data=data)
            if ser.is_valid():
                ser.save()
        elif validated_data['metatype'] == 'file':
            ser = QuickFileMissionSerializer(data=data)
            if ser.is_valid():
                ser.save()
        else:
            pass
        validated_data['data'] = data['name']
        validated_data['user'] = self.context['request'].user

        obj = models.Quick.objects.create(**validated_data)
        return obj
