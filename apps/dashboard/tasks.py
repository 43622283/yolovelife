# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
import json
from datetime import date, timedelta
from django.db.models import Q
from celery.task import periodic_task
from django.conf import settings
from django_redis import get_redis_connection
from scene.models import WorkOrder, Asset, Repository
from scene.serializers.workorder import WorkOrderSerializer

@periodic_task(run_every=settings.WORKORDER_DASHBOARD_COUNT)
def workoder_dashboard():
    conn = get_redis_connection('dashboard')

    # count
    count_dist = dict()
    count_dist['inorder'] = WorkOrder.objects.exclude(_status=settings.TYPE_WORKORDER_DONE).count()
    count_dist['order'] = WorkOrder.objects.count()
    count_dist['repository'] = Repository.objects.count()
    count_dist['asset'] = Asset.objects.count()

    conn.delete('WORKORDER_COUNT')
    conn.set('WORKORDER_COUNT', json.dumps(count_dist))

    # last
    workorder_queryset = WorkOrder.objects.all().order_by('-create_time')[:10]
    workoder_serializer = WorkOrderSerializer(workorder_queryset, many=True)

    conn.delete('WORKORDER_LAST')
    conn.set('WORKORDER_LAST', json.dumps(workoder_serializer.data))

    # months
    count_list = list()
    count = 32
    while count > 0:
        start_time = date.today() - timedelta(days=count)
        end_time = date.today() - timedelta(days=count-1)
        count_list.append({
            'name': start_time.strftime('%m-%d'),
            'wo': WorkOrder.objects.filter(
                Q(create_time__range=(start_time, end_time))
            ).count(),
            'asset': Asset.objects.filter(
                Q(create_time__range=(start_time, end_time)),
            ).count(),
            'repository': Repository.objects.filter(
                Q(create_time__range=(start_time, end_time))
            ).count()
        })
        count = count - 1

    conn.delete('MONTHS_COUNT')
    conn.set('MONTHS_COUNT', json.dumps(count_list))

    # repository
    repository_queryset = Repository.objects.all().order_by('-score')[:10]
    count_list = list()

    for repository in repository_queryset:
        count_list.append({
            'title': repository.title,
            'score': repository.score,
            'status': repository.status,
        })

    conn.delete('REPOSITORY_COUNT')
    conn.set('REPOSITORY_COUNT', json.dumps(count_list))

