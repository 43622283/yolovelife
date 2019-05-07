# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-9-14
# Author Yo
import datetime
from deveops.tools.aliyun_v2.request.cms.base import AliyunCMSTool
from deveops.tools.aliyun_v2.analyze.cms import AnalyzeCMSTool
from django.conf import settings


class AliyunCMSSLBTool(AliyunCMSTool):
    def action_get_metric(self):
        super(AliyunCMSSLBTool, self).action_get_metric()
        self.request.add_query_param('Project', 'acs_slb_dashboard')

    def tool_get_trafficrx(self, instance_id, time):
        self.action_get_metric()
        self.time_select(time)
        self.request.add_query_param('Metric', 'InstanceTrafficRX')
        self.request.add_query_param('Dimensions', str({'instanceId': instance_id}))
        results = self.post()
        yield AnalyzeCMSTool.change_timestamp(results.get('Datapoints'))

    def tool_get_traffictx(self, instance_id, time):
        self.action_get_metric()
        self.time_select(time)
        self.request.add_query_param('Metric', 'InstanceTrafficTX')
        self.request.add_query_param('Dimensions', str({'instanceId': instance_id}))
        results = self.post()
        yield AnalyzeCMSTool.change_timestamp(results.get('Datapoints'))