from django.urls import path
from .api import file as file_api
from .api import image as image_api

urlpatterns=[
    # Resource file api
    path(r'v2/file/', file_api.UtilsFileListAPI.as_view()),
    path(r'v2/file/create/', file_api.UtilsFileCreateAPI.as_view()),
    # Resource image api
    path(r'v2/image/', image_api.UtilsImageListAPI.as_view()),
    path(r'v2/image/create/', image_api.UtilsImageCreateAPI.as_view()),
]