# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
import json
import time
from datetime import datetime, date, timedelta
from django.utils import timezone as datetime
from django.db.models import Q
from celery.task import periodic_task
from django.conf import settings
from django_redis import get_redis_connection
from deveops.tools.aliyun_v2.request.cms.ecs import AliyunCMSECSTool
from manager.models import Group, Host
from scene.models import WorkOrder, Asset, Repository
from scene.serializers import WorkOrderSerializer
from slot.models import Slot
from zdb.models import DBInstance
from ops.models import Push_Mission
from utils.models import FILE
from yodns.models import DNS
from authority.models import ExtendUser


def obj_maker(MODELS, dict_models):
    MODELS.objects.create(**dict_models)


def expired_aliyun_ecs_slot_maker(host):
    from deveops.tools.aliyun_v2.request import ecs
    API = ecs.AliyunECSTool()
    dict_models = API.tool_get_instance_expired_models(host.aliyun_id).__next__()
    if settings.ALIYUN_OVERDUETIME < dict_models.get('expired') < settings.ALIYUN_EXPIREDTIME:
        if Slot.objects.filter(info=settings.LANGUAGE.ExpireAliyunECS.format(
            **dict_models
        ), status=False).exists():
            pass
        else:
            obj_maker(Slot, {
                'group': None,
                'info': settings.LANGUAGE.ExpireAliyunECS.format(
                    **dict_models
                ),
                'type': settings.TYPE_SLOT_EXPIRE,
            })


@periodic_task(run_every=settings.DASHBOARD_EXPIRED_TIME)
def expired_aliyun_ecs():

    for host in Host.objects.filter(Q(groups=None) and ~Q(aliyun_id='')):
        expired_aliyun_ecs_slot_maker(host)

    for group in Group.objects.all():
        for host in group.hosts.filter(~Q(aliyun_id='')):
            expired_aliyun_ecs_slot_maker(host)


#
# @periodic_task(run_every=settings.EXPIRED_TIME)
# def expired_aliyun_rds():
#     ExpiredAliyunRDS.objects.all().delete()
#     from deveops.tools.aliyun_v2.request import rds
#     API = rds.AliyunRDSTool()
#     for dict_models in API.tool_get_instances_expired_models():
#         if not dict_models['readonly']:
#             if settings.ALIYUN_OVERDUETIME < dict_models.get('expired') < settings.ALIYUN_EXPIREDTIME:
#                 obj_maker(ExpiredAliyunRDS, dict_models)
#
#
# @periodic_task(run_every=settings.EXPIRED_TIME)
# def expired_aliyun_kvstore():
#     ExpiredAliyunKVStore.objects.all().delete()
#     from deveops.tools.aliyun_v2.request import kvstore
#     API = kvstore.AliyunKVStoreTool()
#     for dict_models in API.tool_get_instances_expired_models():
#         if settings.ALIYUN_OVERDUETIME < dict_models.get('expired')< settings.ALIYUN_EXPIREDTIME:
#             obj_maker(ExpiredAliyunKVStore, dict_models)
#
#
# @periodic_task(run_every=settings.EXPIRED_TIME)
# def expired_aliyun_mongodb():
#     ExpiredAliyunMongoDB.objects.all().delete()
#     from deveops.tools.aliyun_v2.request import mongodb
#     API = mongodb.AliyunMongoDBTool()
#     for dict_models in API.tool_get_instances_expired_models():
#         if settings.ALIYUN_OVERDUETIME < dict_models.get('expired')< settings.ALIYUN_EXPIREDTIME:
#             obj_maker(ExpiredAliyunMongoDB, dict_models)


@periodic_task(run_every=settings.DASHBOARD_STATS_COUNT)
def statistics_count():
    conn = get_redis_connection('dashboard')
    conn.delete('COUNT')
    count_dist = dict()
    count_dist['GROUP_COUNT'] = Group.objects.count()
    count_dist['HOST_COUNT'] = Host.objects.count()
    count_dist['DNS_COUNT'] = DNS.objects.count()
    count_dist['FILE_COUNT'] = FILE.objects.count()
    count_dist['USER_COUNT'] = ExtendUser.objects.count()
    count_dist['DBINSTANCE_COUNT'] = DBInstance.objects.count()

    for key, value in count_dist.items():
        conn.hset('COUNT', key, value)


week_list = ['Won', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']


@periodic_task(run_every=settings.DASHBOARD_STATS_WORK)
def statistics_work():
    conn = get_redis_connection('dashboard')
    conn.delete('WORK')
    work_dist = dict()
    import django
    now = django.utils.timezone.now().date()
    for i in range(6, -1, -1):
        start_day = now - datetime.timedelta(days=i)
        end_day = now - datetime.timedelta(days=i-1)
        weekday = start_day.weekday()
        work_dist[week_list[int(weekday)]] = Push_Mission.objects.filter(
            create_time__gt=start_day, create_time__lt=end_day
        ).count()
    for key, value in work_dist.items():
        conn.hset('WORK', key, value)


@periodic_task(run_every=settings.DASHBOARD_STATS_GROUP)
def statistics_group():
    conn = get_redis_connection('dashboard')
    conn.delete('GROUP')
    group_dist = {}
    for group in Group.objects.all():
        group_dist[group.name] = group.hosts.count()

    k = sorted(group_dist.items(), key=lambda x: x[1], reverse=True)
    count = 0
    for item in k:
        if count > 5:
            break
        conn.hset('GROUP', item[0], item[1])
        count = count+1


@periodic_task(run_every=settings.DASHBOARD_GROUP_LOAD)
def statistics_group_load():
    conn = get_redis_connection('dashboard')
    for group in Group.objects.all():
        conn.delete('GROUP'+str(group.uuid))
        group_list = list()
        for host in group.hosts.filter(~(Q(aliyun_id='') or Q(aliyun_id__isnull=True)))[:10]:
            API = AliyunCMSECSTool()
            results = API.tool_get_metric_load_5m(host.aliyun_id, 1).__next__()
            group_list.append({
                'title': host.hostname,
                'dataset': results,
            })
            time.sleep(5)

        conn.set(
            'GROUP'+str(group.uuid),
            json.dumps(group_list)
        )


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

