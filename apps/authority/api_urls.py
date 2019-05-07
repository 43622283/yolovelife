from .urls import group
from .urls import jumper
from .urls import key
from .urls import permission
from .urls import role
from .urls import user


urlpatterns = user.urlpatterns +\
              permission.urlpatterns +\
              group.urlpatterns + \
              role.urlpatterns +\
              jumper.urlpatterns +\
              key.urlpatterns
