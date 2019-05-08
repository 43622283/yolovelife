# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-3
# Author Yo
# Email YoLoveLife@outlook.com
from datetime import date
import json
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, status
from django_redis import get_redis_connection
from deveops.api import WebTokenAuthentication
from timeline.decorator import decorator_base
from django.conf import settings
from ..tasks import report_day
__all__ = [

]


class SceneReportDayAPI(WebTokenAuthentication, APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        conn = get_redis_connection('report')
        start_time = date.today()
        if conn.exists('REPORT_{0}_{1}'.format(start_time.strftime('%Y-%m-%d'), request.user.id)):
            data_dict = conn.get('REPORT_{0}_{1}'.format(start_time.strftime('%Y-%m-%d'), request.user.id))
            return Response(
                {'status': '1', 'detail': settings.LANGUAGE.SceneReportDayFormat.format(**json.loads(data_dict))}, status.HTTP_200_OK
            )
        else:
            report_day.delay(request.user.id)
            return Response(
                {'status': '0', 'detail': '您的报告未生成，已经进入生成队列，请稍后获取。'}, status.HTTP_200_OK
            )


class SceneReportWeekAPI(WebTokenAuthentication, APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        return Response(
            {}, status.HTTP_200_OK
        )
