import time
import uuid
from django.conf import settings


def uuid_maker():
    t = time.time()
    return uuid.uuid5(uuid.NAMESPACE_DNS, '{TIME}{SALT}'.format(
        TIME=str(t),
        SALT=settings.UUID_NAME
    ))