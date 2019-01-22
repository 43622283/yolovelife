# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-12-10
# Author Yo
# Email YoLoveLife@outlook.com
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
import uuid
from manager.models import Group


__all__ = [
    'Slot'
]


class Slot(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False)

    group = models.OneToOneField(Group, related_name='slots', on_delete=models.SET_NULL, null=True, blank=True)
    info = models.CharField(max_length=200, default="")

    time = models.DateTimeField(auto_now_add=True, editable=False)
    type = models.IntegerField(default=0)

    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['time', ]

    @property
    def group_name(self):
        if self.group is not None:
            return self.group.name
        else:
            return 'None'
