# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
from django.utils.translation import ugettext_lazy as _
from django.db import models
import uuid
import json
from authority.models import ExtendUser
from django.conf import settings
import django.utils.timezone as timezone
from django_mysql.models import JSONField

__all__ = [
    'Asset', 'WorkOrder',
]


class Asset(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4)

    _status = models.IntegerField(default=settings.STATUS_ASSET_DONE,)

    create_time = models.DateTimeField(auto_now_add=True)

    location = models.CharField(max_length=15, default='', null=True)

    ip_address = models.CharField(max_length=15, default='', null=True)

    mac_address = models.CharField(max_length=25, default='', null=False)

    serial_number = models.CharField(max_length=30, default='', null=True)

    phone = models.CharField(max_length=12, default='', null=True)

    department = models.CharField(max_length=50, default='', null=True)

    user = models.CharField(max_length=50, default='', null=True)

    class Meta:
        permissions = (
            ('deveops_page_asset', u'工作资产页面'),
            ('deveops_api_list_asset', u'罗列工作资产'),
            ('deveops_api_update_asset', u'更新工作资产'),
            ('deveops_api_stop_asset', u'暂停工作资产'),
            ('deveops_api_scrap_asset', u'报废工作资产'),
            ('deveops_api_delete_asset', u'删除工作资产'),
        )

    def update(self, validated_data):
        validated_data['_status'] = settings.STATUS_ASSET_CHANGE_CHECK
        validated_data['type'] = settings.TYPE_ASSET_CHANGE_UPDATE
        AssetChange.objects.create(
            **validated_data
        )
        self._status = settings.STATUS_ASSET_LOCK
        self.save()

    def stop(self):
        AssetChange.objects.create(
            **{
                'uuid': self.uuid,
                'location': self.location,
                'ip_address': self.ip_address,
                'mac_address': self.mac_address,
                'serial_number': self.serial_number,
                'phone': self.phone,
                'department': self.department,
                'user': self.user,
                '_status': settings.STATUS_ASSET_CHANGE_CHECK,
                'type': settings.TYPE_ASSET_CHANGE_STOP
            }
        )
        self._status = settings.STATUS_ASSET_LOCK
        self.save()

    def scrap(self):
        AssetChange.objects.create(
            **{
                'uuid': self.uuid,
                'location': self.location,
                'ip_address': self.ip_address,
                'mac_address': self.mac_address,
                'serial_number': self.serial_number,
                'phone': self.phone,
                'department': self.department,
                'user': self.user,
                '_status': settings.STATUS_ASSET_CHANGE_CHECK,
                'type': settings.TYPE_ASSET_CHANGE_SCRAP
            }
        )
        self._status = settings.STATUS_ASSET_LOCK
        self.save()


class AssetChange(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4)

    create_time = models.DateTimeField(auto_now_add=True)

    type = models.IntegerField(default=settings.TYPE_ASSET_CHANGE_CREATE)

    _status = models.IntegerField(default=settings.STATUS_ASSET_CHANGE_CHECK,)

    location = models.CharField(max_length=15, default='', null=True)

    ip_address = models.CharField(max_length=15, default='', null=True)

    mac_address = models.CharField(max_length=25, default='', null=False)

    serial_number = models.CharField(max_length=30, default='', null=True)

    phone = models.CharField(max_length=12, default='', null=True)

    department = models.CharField(max_length=50, default='', null=True)

    user = models.CharField(max_length=50, default='', null=True)

    def self2install(self):
        self._status = settings.STATUS_ASSET_CHANGE_INSTALL
        self.save()

    def self2config(self):
        self._status = settings.STATUS_ASSET_CHANGE_CONFIG
        self.save()

    def self2done(self):
        self._status = settings.STATUS_ASSET_CHANGE_DONE
        self.save()

    def create(self):
        Asset.objects.create(
            **{
                'location': self.location,
                'ip_address': self.ip_address,
                'mac_address': self.mac_address,
                'serial_number': self.serial_number,
                'phone': self.phone,
                'department': self.department,
                'user': self.user,
                '_status': settings.STATUS_ASSET_DONE,
            }
        )
        self._status = settings.STATUS_ASSET_CHANGE_DONE
        self.save()

    def update(self):
        Asset.objects.filter(uuid=self.uuid).update(
            **{
                'location': self.location,
                'ip_address': self.ip_address,
                'mac_address': self.mac_address,
                'serial_number': self.serial_number,
                'phone': self.phone,
                'department': self.department,
                'user': self.user,
                '_status': settings.STATUS_ASSET_DONE,
            }
        )
        self._status = settings.STATUS_ASSET_CHANGE_DONE
        self.save()

    def stop(self):
        Asset.objects.filter(uuid=self.uuid).update(
            **{
                'location': self.location,
                'ip_address': self.ip_address,
                'mac_address': self.mac_address,
                'serial_number': self.serial_number,
                'phone': self.phone,
                'department': self.department,
                'user': self.user,
                '_status': settings.STATUS_ASSET_STOP
            }
        )
        self._status = settings.STATUS_ASSET_CHANGE_DONE
        self.save()

    def scrap(self):
        Asset.objects.filter(uuid=self.uuid).update(
            **{
                'location': self.location,
                'ip_address': self.ip_address,
                'mac_address': self.mac_address,
                'serial_number': self.serial_number,
                'phone': self.phone,
                'department': self.department,
                'user': self.user,
                '_status': settings.STATUS_ASSET_SCRAP,
            }
        )
        self._status = settings.STATUS_ASSET_CHANGE_DONE
        self.save()

    def connect(self):
        # Link to uuid Asset
        if Asset.objects.filter(uuid=self.uuid).exists():
            obj = Asset.objects.filter(uuid=self.uuid).get()
            from .serializers import asset as asset_serializer
            return asset_serializer.AssetSerializer(obj).data
        else:
            return {}


def upload_sound_path(instance, filename):
    suffix = filename.split('.')[1]
    return 'sound/{0}.{1}'.format(
        str(instance.uuid), suffix
    )


def null_tags():
    return []


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False)
    description = models.TextField(default='', null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(ExtendUser, default=None, blank=True, null=True,
                                    on_delete=models.SET_NULL, related_name='comments')

    class Meta:
        permissions = (
            ('deveops_api_list_comment', u'罗列评论'),
            ('deveops_api_create_comment', u'更新评论'),
            ('deveops_api_delete_comment', u'删除评论'),
        )


class Classify(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4)
    name = models.CharField(max_length=13, default='', null=True)

    class Meta:
        permissions = (
            ('deveops_api_list_classify', u'罗列工单分类'),
            ('deveops_api_create_classify', u'创建工单分类'),
            ('deveops_api_delete_classify', u'删除工单分类'),
        )


class WorkOrder(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False)

    classify = models.ForeignKey(Classify, default=None, blank=True, null=True,
                                    on_delete=models.SET_NULL, related_name='workorders')

    duty_user = models.ForeignKey(ExtendUser, default=None, blank=True, null=True,
                                    on_delete=models.SET_NULL, related_name='workorders')

    sound = models.FileField(upload_to=upload_sound_path, null=True, blank=True)

    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(auto_now=True)

    # Select from Asset
    location = models.CharField(max_length=15, default='', blank=True, null=True)

    serial_number = models.CharField(max_length=30, default='', null=True, blank=True)

    src_phone = models.CharField(max_length=12, default='', null=True)

    phone = models.CharField(max_length=12, default='', null=True)

    department = models.CharField(max_length=50, default='', null=True)

    user = models.CharField(max_length=50, default='', null=True)

    ip_address = models.CharField(max_length=15, default='', null=True, blank=True)

    mac_address = models.CharField(max_length=25, default='', null=False, blank=True)

    _status = models.IntegerField(default=settings.TYPE_WORKORDER_INACTIVE,)

    # Detail
    title = models.CharField(max_length=200, default='', null=True, blank=True)

    description = models.CharField(max_length=2000, default='', null=True, blank=True)

    comments = models.ManyToManyField(Comment, blank=True,
                                      related_name='workorders', verbose_name=_("workorders"))

    tags = JSONField(default=null_tags)

    class Meta:
        permissions = (
            ('deveops_page_workorder', u'现场工单页面'),
            ('deveops_api_list_workorder', u'罗列现场工单'),
            ('deveops_api_create_workorder', u'创建现场工单'),
            ('deveops_api_update_workorder', u'更新现场工单'),
        )

    def active(self):
        if self._status == settings.TYPE_WORKORDER_INACTIVE:
            self._status = settings.TYPE_WORKORDER_RUN

    def fail(self):
        if self._status == settings.TYPE_WORKORDER_INACTIVE:
            self._status = settings.TYPE_WORKORDER_FAIL

    def done(self):
        if self._status == settings.TYPE_WORKORDER_RUN:
            self._status = settings.TYPE_WORKORDER_DONE

    def turn(self, turn_obj):
        # obj = ExtendUser.objects.get(id=turn_id)
        self.duty_user = turn_obj


class Repository(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, default='', null=True, blank=True)
    description = models.TextField(default='', null=True, blank=True)
    score = models.FloatField(default=0)
    comments = models.ManyToManyField(Comment, blank=True,
                                      related_name='repositorys', verbose_name=_("repositorys"))

    user = models.ForeignKey(ExtendUser, default=None, blank=True, null=True,
                                    on_delete=models.SET_NULL, related_name='repositorys')

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    status = models.IntegerField(default=settings.STATUS_REPOSITORY_OK)
    tags = JSONField(default=null_tags)

    class Meta:
        permissions = (
            ('deveops_page_repository', u'现场知识库页面'),
            ('deveops_api_list_repository', u'罗列知识库'),
            ('deveops_api_create_repository', u'创建知识库'),
            ('deveops_api_update_repository', u'更新知识库'),
            ('deveops_api_delete_repository', u'删除知识库'),
        )

    @property
    def comment_count(self):
        return self.comments.count()

    def ok(self):
        if self.status == settings.STATUS_REPOSITORY_EXPIRED or \
                self.status == settings.STATUS_REPOSITORY_MAINTENANCE:
            self.status = settings.STATUS_REPOSITORY_OK

    def expired(self):
        if self.status == settings.STATUS_REPOSITORY_OK:
            self.status = settings.STATUS_REPOSITORY_EXPIRED

    def maintenance(self):
        if self.status == settings.STATUS_REPOSITORY_OK:
            self.status = settings.STATUS_REPOSITORY_MAINTENANCE


class Record(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False)
    sound = models.FileField(upload_to=upload_sound_path, null=True, blank=True)
    phone = models.CharField(max_length=12, default='', null=True)

    create_time = models.DateTimeField(default=timezone.now)

    solved = models.BooleanField(default=False)

    def workorder(self):
        obj_filter = Asset.objects.filter(phone=self.phone)
        if obj_filter.exists():
            print('exists')
            obj = obj_filter.get()
            WorkOrder.objects.create(
                **{
                    'location': obj.location,
                    'ip_address': obj.ip_address,
                    'mac_address': obj.mac_address,
                    'serial_number': obj.serial_number,
                    'phone': obj.phone,
                    'src_phone': obj.phone,
                    'department': obj.department,
                    'user': obj.user,
                    'sound': self.sound,
                    'create_time': self.create_time
                })
        else:
            print('no_exists')
            WorkOrder.objects.create(**{
                'sound': self.sound,
                'create_time': self.create_time,
                'phone': self.phone,
                'src_phone': self.phone,
            })
        self.solved = True
        self.save()
