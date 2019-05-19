# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-11-16
# Author Yo
# Email YoLoveLife@outlook.com


def decorator_base(ClassName, timeline_type):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            instances, msg, response = func(*args, **kwargs)
            if 100 < response.status_code < 300:
                obj = ClassName.objects.create(type=timeline_type, msg=msg)
                obj.instances.set(instances)
            return response
        return inner_wrapper
    return wrapper
