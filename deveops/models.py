# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
import pyotp
from django.db import models
from deveops.utils.uuid_maker import uuid_maker

__all__ = [

]


class BaseModal(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid_maker)

    _visible = models.BooleanField(default=True)

    def visible(self):
        self._visible = False

    class Meta:
        abstract = True
