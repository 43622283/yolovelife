from django.urls import path
from .api import notice as NoticeAPI
from .api import remind as RemindAPI
urlpatterns = [
    # Resource notice api
    path(r'v1/notice/list', NoticeAPI.NoticeListAPI.as_view()),
    path(r'v1/notice/create/', NoticeAPI.NoticeCreateAPI.as_view()),

    # Resource remind api
    path(r'v1/remind/list', RemindAPI.RemindListAPI.as_view()),
    path(r'v1/remind/create/', RemindAPI.RemindCreateAPI.as_view()),
]
