# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import asset as AssetAPI
from ..api import assetchange as AssetChangeAPI
from ..api import workorder as WorkOrderAPI
from ..api import repository as RepositoryAPI
from ..api import comment as CommentAPI
from ..api import report as ReportAPI
from ..api import record as RecordAPI

urlpatterns = [
    # Resource comment api
    # path(r'v2/comment/', CommentAPI.SceneCommentListAPI.as_view()),
    # path(r'v2/comment/create/', CommentAPI.SceneCommentCreateAPI.as_view()),
    # path(r'v2/comment/<uuid:pk>/update/', CommentAPI.SceneCommentUpdateAPI.as_view()),
    path(r'v2/comment/<uuid:pk>/delete/', CommentAPI.SceneCommentDeleteAPI.as_view()),
]
