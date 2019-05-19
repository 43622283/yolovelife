# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-05-18
# Author Yo
import json
from celery.task import periodic_task
from django.conf import settings
from django_redis import get_redis_connection
from .models import Department, User
from .serializers import department as department_serializer
import pymssql

DEPARTMENT_SQL = '''
    select * from [Department]
'''

@periodic_task(run_every=settings.ORGANIZATION_SYNC)
def organization_department():
    conn = pymssql.connect(
        **settings.ORGANIZATION_SETTING
    )
    cursor = conn.cursor()
    cursor.execute(DEPARTMENT_SQL)
    result_set = cursor.fetchall()
    for result in result_set:
        if Department.objects.filter(
            id=result[0]
        ).exists():
            Department.objects.filter(
                id=result[0],
                father_id=result[1],
            ).update(
                name=result[2],
                create_time=result[9],
            )
        else:
            if result[1] != 0:
                Department.objects.create(
                    id=result[0],
                    father_id=result[1],
                    name=result[2],
                    create_time=result[9],
                )
            else:
                Department.objects.create(
                    id=result[0],
                    name=result[2],
                    create_time=result[9],
                )
    conn.close()

# For Celery maximum recursion depth exceede
def get_data(queryset):
    return department_serializer.DepartmentSerializer(queryset, many=True)

@periodic_task(run_every=settings.ORGANIZATION_SYNC)
def organization_department_cache():
    conn = get_redis_connection('organization')
    department_queryset = Department.objects.filter(
        father__isnull=True
    )
    serializer = get_data(department_queryset)

    conn.set(
        'ORGANIZATION_DEPARTMENT',
        json.dumps(serializer.data),
    )


USER_SQL = '''
    select * from [User]
'''

@periodic_task(run_every=settings.ORGANIZATION_SYNC)
def organization_user():
    conn = pymssql.connect(
        **settings.ORGANIZATION_SETTING
    )
    cursor = conn.cursor()
    cursor.execute(USER_SQL)
    result_set = cursor.fetchall()
    for result in result_set:
        print(result[-3])
        if User.objects.filter(
            uuid=result[0]
        ).exists():
            User.objects.filter(
                uuid=result[0],
            ).update(
                **{
                    'username': result[1],
                    'name': result[3],
                    'office_phone': result[7],
                    'phone': result[11],
                    'sub_phone': result[12],
                    'home_phone': result[12],
                    'email': result[15],
                    'sex': result[16],
                    'office': result[17],
                    'department_id': result[18],
                    'location': result[-3] or '000',
                }
            )
        else:
            User.objects.create(
                **{
                    'uuid': result[0],
                    'username': result[1],
                    'name': result[3],
                    'office_phone': result[7],
                    'phone': result[11],
                    'sub_phone': result[12],
                    'home_phone': result[12],
                    'email': result[15],
                    'sex': result[16],
                    'office': result[17],
                    'department_id': result[18],
                    'location': result[-3] or '000',
                }
            )
    conn.close()