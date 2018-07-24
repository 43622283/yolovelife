# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-24
# Author Yo
# Email YoLoveLife@outlook.com
# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deveops.settings")
# django.setup()

import json
from aliyunsdkcore import client
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import AuthorizeSecurityGroupEgressRequest
from django.conf import settings


class AliyunSafeTool(object):
    def __init__(self):
        self.clt = client.AcsClient(settings.ALIYUN_ACCESSKEY, settings.ALIYUN_ACCESSSECRET, 'cn-hangzhou')

    @staticmethod
    def request_to_json(request):
        return request.set_accept_format('json')

    @staticmethod
    def get_json_results(results):
        return json.loads(results.decode('utf-8'))


    def request_attend_egress_policy(self, safekwargs):
        request = AuthorizeSecurityGroupEgressRequest.AuthorizeSecurityGroupEgressRequest()
        self.request_to_json(request)
        request.add_query_param('RegionId', 'cn-hangzhou')

        safekwargs.add_query_param(request)

        try:
            response = self.clt.do_action_with_exception(request)
        except ServerException as e:
            print(e)
            return {}

        return self.get_json_results(response)