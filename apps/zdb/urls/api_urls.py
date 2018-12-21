from django.urls import path
from zdb.api import instance as InstanceAPI
from zdb.api import database as DatabaseAPI
urlpatterns = [
    # Resource ZDB Instance api
    path(r'v1/instance/', InstanceAPI.ZDBInstanceListAPI.as_view()),
    path(r'v1/instance/bypage/', InstanceAPI.ZDBInstanceListByPageAPI.as_view()),
    path(r'v1/instance/flush/', InstanceAPI.ZDBInstanceFlushDatabaseAPI.as_view()),
    path(r'v1/instance/create/', InstanceAPI.ZDBInstanceCreateAPI.as_view()),
    path(r'v1/instance/<uuid:pk>/update/', InstanceAPI.ZDBInstanceUpdateAPI.as_view()),
    path(r'v1/instance/<uuid:pk>/delete/', InstanceAPI.ZDBInstanceDeleteAPI.as_view()),
    # Resource ZDB Database api
    path(r'v1/database/', DatabaseAPI.ZDBDatabaseListAPI.as_view()),
    path(r'v1/database/bypage/', DatabaseAPI.ZDBDatabaseListByPageAPI.as_view()),
]