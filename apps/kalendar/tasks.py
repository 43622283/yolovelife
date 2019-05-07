# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
import time
import os
import json
from datetime import datetime, date, timedelta
from django.db.models import Q
from django_redis import get_redis_connection
from django.conf import settings
from kalendar import models, serializers
from celery import Task, task

class KalendarTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))


@task(base=KalendarTask)
def kalendar_push(time):
    conn = get_redis_connection('kalendar')
    kalendar_queryset = models.Kalendar.objects.filter(
        time__year=time.year,
        time__month=time.month,
        time__day=time.day
    )

    kalendar_serializer = serializers.KalendarSerializer(kalendar_queryset, many=True)
    print(kalendar_serializer.data)
    conn.set(time.strftime('%Y-%m-%d'), json.dumps(kalendar_serializer.data))
