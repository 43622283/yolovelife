# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-3
# Author Yo
# Email YoLoveLife@outlook.com
from deveops.models import BaseModal

__all__ = [
    'Dashboard'
]


class Dashboard(BaseModal):

    class Meta:
        permissions = (
            ('deveops_page_dashboard', u'仪表盘'),
        )