# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import asset as AssetAPI
from ..api import assetchange as AssetChangeAPI

urlpatterns = [
    # Resource asset api
    path(r'v1/asset/', AssetAPI.SceneAssetListAPI.as_view()),
    path(r'v1/asset/bypage/', AssetAPI.SceneAssetListByPageAPI.as_view()),
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
]
