from django.urls import path
from ..api import slot as SlotAPI

urlpatterns = [
    # Resource host api
    path(r'v1/slot/bypage/', SlotAPI.SlotListByPageAPI.as_view()),
    path(r'v1/slot/<uuid:pk>/check/', SlotAPI.SlotCheckAPI.as_view()),
]