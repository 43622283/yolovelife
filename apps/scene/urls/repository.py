# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import repository as RepositoryAPI

urlpatterns = [
    path(r'v2/repository/list/', RepositoryAPI.SceneRepositoryListAPI.as_view()),
    path(r'v2/repository/create/', RepositoryAPI.SceneRepositoryCreateAPI.as_view()),
    path(r'v2/repository/<uuid:pk>/detail/', RepositoryAPI.SceneRepositoryDetailAPI.as_view()),
    path(r'v2/repository/<uuid:pk>/update/', RepositoryAPI.SceneRepositoryUpdateAPI.as_view()),
    path(r'v2/repository/<uuid:pk>/stars/', RepositoryAPI.SceneRepositoryStarsAPI.as_view()),
    path(r'v2/repository/<uuid:pk>/delete/', RepositoryAPI.SceneRepositoryDeleteAPI.as_view()),
    path(r'v2/repository/<uuid:pk>/comment/create/', RepositoryAPI.SceneRepositoryCommentAPI.as_view()),
    path(r'v2/repository/<uuid:pk>/ok/', RepositoryAPI.SceneRepositoryBeOkAPI.as_view()),
    path(r'v2/repository/<uuid:pk>/expired/', RepositoryAPI.SceneRepositoryBeExpiredAPI.as_view()),
    path(r'v2/repository/<uuid:pk>/maintenance/', RepositoryAPI.SceneRepositoryBeMaintenanceAPI.as_view()),
]
