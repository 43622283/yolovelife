# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-1-15
# Author Yo
from deveops.tools.qingcloud.request.base import QingCloudTool
from deveops.tools.qingcloud.analyze.instance import AnalyzeInstanceTool
from django.conf import settings


class QingCloudInstanceTool(QingCloudTool):
    def tool_get_instances_models(self):
        offset = 0
        for count in range(1, 9999):
            ret = self.clt.describe_instances(offset=offset, limit=settings.QINGCLOUD_PAGESIZE)
            for instance in ret['instance_set']:
                if instance['instance_type'] == 'custom' or instance['status'] == 'ceased':
                    pass
                else:
                    yield AnalyzeInstanceTool.get_models(instance)
            offset += settings.QINGCLOUD_PAGESIZE
            if offset >= ret['total_count']:
                break




