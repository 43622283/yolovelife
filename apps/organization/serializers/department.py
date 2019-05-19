# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-3
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from .. import models

__all__ = [
    'DepartmentSerializer',
]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ('id', 'uuid', 'name')

    def get_fields(self):
        fields = super(DepartmentSerializer, self).get_fields()
        fields['subdepartment'] = DepartmentSerializer(many=True)
        return fields
