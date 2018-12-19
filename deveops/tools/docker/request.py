# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-12-19
# Author Yo
# Email YoLoveLife@outlook.com
import docker
from deveops.tools.docker.analyze import DockerAnalyzeTool
__all__ = [
    'DockerRequestTool',
]


class DockerRequestTool(object):
    def __init__(self, base_url='tcp://127.0.0.1:2375', version='auto'):
        self.clt = docker.DockerClient(base_url=base_url, version=version)

    def tool_get_image_list(self):
        images = self.clt.images.list()
        for obj in images:
            yield DockerAnalyzeTool.get_image_models(obj)

    def tool_get_container_list(self):
        containers = self.clt.containers.list(all=True)
        for obj in containers:
            yield DockerAnalyzeTool.get_container_models(obj)

    def tool_get_container_top(self, container_id_or_name):
        container = self.clt.containers.get(container_id_or_name)
        yield container.top()

    def tool_get_container_stats(self, container_id_or_name):
        container = self.clt.containers.get(container_id_or_name)
        yield container.stats()

    def tool_kill_container(self, container_id_or_name):
        container = self.clt.containers.get(container_id_or_name)
        if container.status == 'running':
            container.kill('SIGKILL')
        elif container.status == 'exited':
            pass
        else:
            pass

    def tool_start_container(self, container_id_or_name):
        container = self.clt.containers.get(container_id_or_name)
        if container.status == 'exited':
            container.start()
        else:
            pass

    def tool_stop_container(self, container_id_or_name):
        container = self.clt.containers.get(container_id_or_name)
        if container.status == 'running':
            container.stop()
        else:
            pass

    def tool_remove_container(self, container_id_or_name):
        container = self.clt.containers.get(container_id_or_name)
        if container.status == 'exited':
            container.remove()

    def tool_run_container(
            self, *args, **kwargs):
        self.clt.run(kwargs)




API = DockerRequestTool()
print(API.tool_get_container_stats('ff076e1fb5de').__next__())
# for m in API.tool_get_container_list():
#     print(m.stats())


