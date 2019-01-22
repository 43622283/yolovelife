# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-7-2
# Author Yo
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deveops.settings")
django.setup()


class AnalyzeTool(object):
    @staticmethod
    def get_expired_day(time):
        pass

    @staticmethod
    def get_models(result):
        pass

    @staticmethod
    def get_expired_models(result):
        pass