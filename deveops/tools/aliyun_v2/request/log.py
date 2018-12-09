# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-11-08
# Author Yo
# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deveops.settings")
# django.setup()
from deveops.tools.aliyun_v2.request.base import AliyunTool
from django.conf import settings
from aliyun.log.logitem import LogItem
from aliyun.log.logclient import LogClient
from aliyun.log.getlogsrequest import GetLogsRequest
from aliyun.log.putlogsrequest import PutLogsRequest
from aliyun.log.listlogstoresrequest import ListLogstoresRequest
from aliyun.log.gethistogramsrequest import GetHistogramsRequest


class AliyunLOGTool(AliyunTool):

    def __init__(self):
        self.clt = LogClient('cn-hangzhou.log.aliyuncs.com', settings.ALIYUN_ACCESSKEY, settings.ALIYUN_ACCESSSECRET)

    # def init_action(self):
    #
    #     self.request.set_domain('cn-hangzhou.log.aliyuncs.com')
    #     self.request.set_method('GET')
    #     self.request.set_version('2018-01-01')

    def action_get_logs(self):
        pass

    def tool_get_logs(self, project, logstore, From, To, Topic, SQL):
        self.action_get_logs()
        req = GetLogsRequest(project, logstore, From, To, Topic, SQL, 10, 0, False)
        res = self.clt.get_logs(req)
        return res.get_body()


# API = AliyunLOGTool()
# import time
# From = int(time.time()) - 600
# To = int(time.time())
# results = API.tool_get_logs('xmt-cloud', 'vote', From, To, '', "* | select count(1) as pv, request_uri as path  group by request_uri order by pv desc limit 10")
# print(results.get_body())
