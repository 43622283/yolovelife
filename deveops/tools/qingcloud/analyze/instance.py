# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-1-14
# Author Yo
import datetime
from deveops.tools.qingcloud.analyze.base import AnalyzeTool
from django.conf import settings


class AnalyzeInstanceTool(AnalyzeTool):

    @staticmethod
    def get_instance_status(status):
        if status == 'running':
            return settings.STATUS_HOST_CAN_BE_USE
        else:
            return settings.STATUS_HOST_CLOSE

    @staticmethod
    def get_models(json_results):
        # print(json_results)
        try:
            ipaddr = json_results['vxnets'][0]['private_ip']
        except Exception as e:
            ipaddr = ''
        try:
            image = json_results['image']['image_name']
        except Exception as e:
            image = ''

        return {
            'hostname': json_results['instance_name'],
            'connect_ip': ipaddr,
            'sshport': 22,
            'status': AnalyzeInstanceTool.get_instance_status(json_results['status']),
            'systemtype': image,
            'position': 'Qing云',
            'qingcloud_id': json_results['instance_id'],
        }


    @staticmethod
    def get_security_models(json_results):
        return {
            'security_id': json_results.get('SecurityGroupId'),
            'security_name': json_results.get('SecurityGroupName'),
            'vpc_id': json_results.get('VpcId')
        }