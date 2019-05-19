# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
import pyotp
from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django_redis import get_redis_connection
from deveops.utils import aes
from django.conf import settings
from deveops.models import BaseModal
from deveops.utils.uuid_maker import uuid_maker
from .tasks import jumper_status_flush
from .utils import private_key_validator, public_key_validator

__all__ = [
    "Key", "ExtendUser", "Jumper", "Group"
]


class Key(BaseModal):
    name = models.CharField(max_length=100, default='')
    _private_key = models.TextField(max_length=4096, blank=True, null=True,
                                    validators=[private_key_validator, ])
    _public_key = models.TextField(max_length=4096, blank=True, null=True,
                                   validators=[public_key_validator, ])
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (
            ('deveops_api_list_key', u'罗列密钥'),
            ('deveops_api_create_key', u'创建密钥'),
            ('deveops_api_update_key', u'更新密钥'),
            ('deveops_api_delete_key', u'删除密钥'),
            ('deveops_page_key', u'秘钥页面'),
        )

    @property
    def private_key(self):
        if self._private_key:
            key_str = aes.decrypt(self._private_key)
            return key_str
        else:
            return None

    @private_key.setter
    def private_key(self, private_key):
        self._private_key = aes.encrypt(private_key).decode()

    @property
    def public_key(self):
        return aes.decrypt(self._public_key)

    @public_key.setter
    def public_key(self, public_key):
        self._public_key = aes.encrypt(public_key).decode()


class ExtendUser(AbstractUser):
    uuid = models.UUIDField(auto_created=True, default=uuid_maker)
    img = models.CharField(max_length=10, default='user.jpg')
    phone = models.CharField(max_length=11, default='None',)
    full_name = models.CharField(max_length=11, default='未获取')
    qrcode = models.CharField(max_length=16, default='')
    have_qrcode = models.BooleanField(default=False)
    expire = models.IntegerField(default=100)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_set",
        related_query_name="user",
    )
    info = models.CharField(default='', max_length=150)
    _visible = models.BooleanField(default=True)

    class Meta:
        permissions = (
            ('deveops_api_list_user', u'罗列用户'),
            ('deveops_api_create_user', u'新增用户'),
            ('deveops_api_update_user', u'修改用户'),
            ('deveops_api_delete_user', u'删除用户'),
            # django.contrib.auth.models.Permission django.contrib.auth.models.Group 无法重构
            ('deveops_api_list_role', u'罗列角色'),
            ('deveops_api_create_role', u'新增角色'),
            ('deveops_api_update_role', u'修改角色'),
            ('deveops_api_list_permission', u'罗列权限'),
            ('deveops_page_role', u'角色页面'),
            ('deveops_page_user', u'用户页面'),
        )

    def visible(self):
        self._visible = False

    def get_8531email(self):
        return self.username + '@8531.cn'

    def get_group_name(self):
        if self.is_superuser == 1:
            return "超级管理员"
        elif self.groups.count() == 0:
            return "无权限"
        else:
            gourp_list = []
            groups = self.groups.all()
            for group in groups:
                gourp_list.append(group.name)
            if len(gourp_list) == 0:
                return ''
            else:
                return "-".join(gourp_list)

    def check_qrcode(self, verifycode):
        t = pyotp.TOTP(self.qrcode)
        result = t.verify(verifycode)
        return result

    @property
    def is_expire(self):
        conn = get_redis_connection('user')
        return not conn.exists(self.username)

    @is_expire.setter
    def is_expire(self, qrcode):
        conn = get_redis_connection('user')
        conn.set(self.username, qrcode, self.expire or 1)

    def get_api_permissions(self, obj=None):
        permission = self.get_all_permissions(obj)
        return [
            p for p in permission if 'api_' in p
        ]

    def get_page_permissions(self, obj=None):
        permission = self.get_all_permissions(obj)
        return [
            p for p in permission if 'page_' in p
        ]


class Jumper(BaseModal):
    connect_ip = models.GenericIPAddressField(default='0.0.0.0')
    sshport = models.IntegerField(default='52000')
    name = models.CharField(max_length=50, default="")
    info = models.CharField(max_length=200, default="", blank=True, null=True)
    _status = models.IntegerField(default=settings.STATUS_JUMPER_NO_KEY)

    class Meta:
        permissions = (
            ('deveops_api_list_jumper', u'罗列跳板机'),
            ('deveops_api_create_jumper', u'创建跳板机'),
            ('deveops_api_update_jumper', u'更新跳板机'),
            ('deveops_api_status_jumper', u'刷新跳板机器'),
            ('deveops_api_delete_jumper', u'删除跳板机'),
            ('deveops_page_jumper', u'跳板机页面'),
        )

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self):
        self.check_status()

    def check_status(self):
        jumper_status_flush.delay(self)

    def to_yaml(self):
        return {
            u'set_fact':
                {
                    'ansible_ssh_common_args':
                        '-o ProxyCommand="ssh -p{{JUMPER_PORT}} -i {{KEY}} -W %h:%p root@{{JUMPER_IP}}"'
                }
        }

