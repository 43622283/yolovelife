# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-2
# Author Yo
from django.conf import settings
from qingcloud.iaas.connection import APIConnection


def connect_to_zone(zone, access_key_id, secret_access_key, lowercase=True):
    """ Connect to one of zones in qingcloud by access key.
    """
    if lowercase:
        zone = zone.strip().lower()
    return APIConnection(access_key_id, secret_access_key, zone, host='api.zhebaoyun.com', port=7777, protocol='http',)


class QingCloudTool(object):
    def __init__(self):
        self.clt = connect_to_zone(
            'zbjta',
            settings.QINGCLOUD_ACCESSKEY,
            settings.QINGCLOUD_ACCESSSECRET,
        )
