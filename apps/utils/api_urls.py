from django.urls import path
from . import api as file_api

urlpatterns=[
    # Resource file api
    path(r'v1/file/', file_api.UtilsFileListAPI.as_view()),
    path(r'v1/file/create/', file_api.UtilsFileCreateAPI.as_view()),
]