# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-12-10
# Author Yo
# Email YoLoveLife@outlook.com

from __future__ import absolute_import, unicode_literals
import json
from celery import Task, task
from django_redis import get_redis_connection
from notify import serialiers


class JumperTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))


@task(base=JumperTask)
def remind(remind_obj):
    conn = get_redis_connection('notify')
    data = serialiers.RemindSerializer(remind_obj)
    if remind_obj.groups.exists():
        for group in remind_obj.groups.all():
            for user in group.user_set.all():
                conn.sadd(
                    'remind_{0}_{1}'.format(
                        user.username, user.id
                    ),
                    json.dumps(data)
                )
    if remind_obj.users.exists():
        for user in remind_obj.users.all():
            conn.sadd(
                'remind_{0}_{1}'.format(
                    user.username, user.id
                ),
                json.dumps(data),
            )

    remind_obj.visible()

