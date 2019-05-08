from .urls import type
from .urls import developer
from .urls import envirtual
from .urls import location

urlpatterns = type.urlpatterns + \
              developer.urlpatterns + \
              envirtual.urlpatterns + \
              location.urlpatterns




