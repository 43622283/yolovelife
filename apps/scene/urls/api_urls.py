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
    # Resource asset api
    path(r'v1/asset/', AssetAPI.SceneAssetListAPI.as_view()),
    path(r'v1/asset/bypage/', AssetAPI.SceneAssetListByPageAPI.as_view()),
    # path(r'v1/asset/<uuid:pk>/delete/', AssetAPI.SceneAssetDeleteAPI.as_view()),
    path(r'v1/asset/change/bypage/', AssetChangeAPI.SceneAssetChangeListByPageAPI.as_view()),
    path(r'v1/asset/change/create/2install/', AssetChangeAPI.SceneAssetChangeCreate2InstallAPI.as_view()),
    path(r'v1/asset/change/create/<uuid:pk>/2config/', AssetChangeAPI.SceneAssetChangeCreate2ConfigAPI.as_view()),
    path(r'v1/asset/change/create/<uuid:pk>/2done/', AssetChangeAPI.SceneAssetChangeCreate2DoneAPI.as_view()),
    path(r'v1/asset/change/update/<uuid:pk>/2check/', AssetChangeAPI.SceneAssetChangeUpdate2CheckAPI.as_view()),
    path(r'v1/asset/change/update/<int:pk>/2done/', AssetChangeAPI.SceneAssetChangeUpdate2DoneAPI.as_view()),
    path(r'v1/asset/change/stop/<uuid:pk>/2check/', AssetChangeAPI.SceneAssetChangeStop2CheckAPI.as_view()),
    path(r'v1/asset/change/stop/<int:pk>/2done/', AssetChangeAPI.SceneAssetChangeStop2DoneAPI.as_view()),
    path(r'v1/asset/change/scrap/<uuid:pk>/2check/', AssetChangeAPI.SceneAssetChangeScrap2CheckAPI.as_view()),
    path(r'v1/asset/change/scrap/<int:pk>/2done/', AssetChangeAPI.SceneAssetChangeScrap2DoneAPI.as_view()),


    # Resource workorder api
    path(r'v1/workorder/', WorkOrderAPI.SceneWorkOrderListAPI.as_view()),
    path(r'v1/workorder/bypage/', WorkOrderAPI.SceneWorkOrderListByPageAPI.as_view()),
    path(r'v1/workorder/create/', WorkOrderAPI.SceneWorkOrderCreateAPI.as_view()),
    path(r'v1/workorder/mobile/detail/', WorkOrderAPI.SceneWorkOrderMobileDetailAPI.as_view()),
    path(r'v1/workorder/<uuid:pk>/detail/', WorkOrderAPI.SceneWorkOrderDetailAPI.as_view()),
    path(r'v1/workorder/<uuid:pk>/update/', WorkOrderAPI.SceneWorkOrderUpdateAPI.as_view()),
    path(r'v1/workorder/<uuid:pk>/active/', WorkOrderAPI.SceneWorkOrderActiveAPI.as_view()),
    path(r'v1/workorder/<uuid:pk>/appoint/', WorkOrderAPI.SceneWorkOrderAppointAPI.as_view()),
    path(r'v1/workorder/<uuid:pk>/done/', WorkOrderAPI.SceneWorkOrderDoneAPI.as_view()),
    path(r'v1/workorder/<uuid:pk>/comment/create/', WorkOrderAPI.SceneWorkOrderCommentAPI.as_view()),
    # path(r'v1/workorder/<uuid:pk>/delete/', WorkOrderAPI.SceneWorkOrderDeleteAPI.as_view()),

    # Resource repository api
    path(r'v1/repository/bypage/', RepositoryAPI.SceneRepositoryListByPageAPI.as_view()),
    path(r'v1/repository/create/', RepositoryAPI.SceneRepositoryCreateAPI.as_view()),
    path(r'v1/repository/<uuid:pk>/detail/', RepositoryAPI.SceneRepositoryDetailAPI.as_view()),
    path(r'v1/repository/<uuid:pk>/update/', RepositoryAPI.SceneRepositoryUpdateAPI.as_view()),
    path(r'v1/repository/<uuid:pk>/stars/', RepositoryAPI.SceneRepositoryStarsAPI.as_view()),
    path(r'v1/repository/<uuid:pk>/delete/', RepositoryAPI.SceneRepositoryDeleteAPI.as_view()),
    path(r'v1/repository/<uuid:pk>/comment/create/', RepositoryAPI.SceneRepositoryCommentAPI.as_view()),
    path(r'v1/repository/<uuid:pk>/ok/', RepositoryAPI.SceneRepositoryBeOkAPI.as_view()),
    path(r'v1/repository/<uuid:pk>/expired/', RepositoryAPI.SceneRepositoryBeExpiredAPI.as_view()),
    path(r'v1/repository/<uuid:pk>/maintenance/', RepositoryAPI.SceneRepositoryBeMaintenanceAPI.as_view()),

    # Resource comment api
    # path(r'v1/comment/', CommentAPI.SceneCommentListAPI.as_view()),
    # path(r'v1/comment/create/', CommentAPI.SceneCommentCreateAPI.as_view()),
    # path(r'v1/comment/<uuid:pk>/update/', CommentAPI.SceneCommentUpdateAPI.as_view()),
    path(r'v1/comment/<uuid:pk>/delete/', CommentAPI.SceneCommentDeleteAPI.as_view()),

    # Resource report api
    path(r'v1/report/day/', ReportAPI.SceneReportDayAPI.as_view()),
    path(r'v1/report/week/', ReportAPI.SceneReportDayAPI.as_view()),

    # Resource record api
    path(r'v1/record/create/', RecordAPI.SceneRecordCreateAPI.as_view()),
]
