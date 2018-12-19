# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-12-19
# Author Yo
# Email YoLoveLife@outlook.com
import docker

__all__ = [
    'DockerAnalyzeTool',
]


class DockerAnalyzeTool(object):

    @staticmethod
    def get_image_models(obj):
        return {
            'sid': obj.id[7:],
            'name': obj.tags[0],
        }

    @staticmethod
    def get_container_models(obj):
        print(dir(obj))
        return {
            'cid': obj.id,
            'labels': obj.labels,
            'name': obj.name,
            'status': obj.status,
        }
