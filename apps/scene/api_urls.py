from .urls import asset
from .urls import comment
from .urls import record
from .urls import report
from .urls import repository
from .urls import workorder
from .urls import classify


urlpatterns = asset.urlpatterns + \
              comment.urlpatterns + \
              record.urlpatterns + \
              report.urlpatterns + \
              repository.urlpatterns + \
              workorder.urlpatterns + \
              classify.urlpatterns

