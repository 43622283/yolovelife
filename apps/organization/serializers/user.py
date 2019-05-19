# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-3
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from .. import models

__all__ = [
    'UserSerializer',
]

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'id', 'uuid', 'username', 'name', 'sex', 'organization',
            'office_phone', 'phone', 'sub_phone', 'home_phone',
            'email', 'location', 'office'
        )