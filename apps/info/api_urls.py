from .urls import type
from .urls import developer
from .urls import envirtual
from .urls import location
from .urls import info

urlpatterns = type.urlpatterns + \
              developer.urlpatterns + \
              envirtual.urlpatterns + \
              location.urlpatterns + \
              info.urlpatterns




