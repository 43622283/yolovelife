from celery.schedules import crontab
#
DASHBOARD_STATS_COUNT = crontab(hour="*", day_of_week="sunday")

DASHBOARD_STATS_WORK = crontab(minute="*/30", day_of_week="sunday")

DASHBOARD_STATS_GROUP = crontab(minute="*/30", day_of_week="sunday")

DASHBOARD_GROUP_LOAD = crontab(minute="*")

MANAGER_HOST_TIME = crontab(minute='*/30', day_of_week="sunday")

MANAGER_HOST_SSH_CHECK = crontab(minute='*/10', day_of_week="sunday")

MANAGER_HOST_LOAD_CHECK = crontab(minute='*/30', day_of_week="sunday")

MANAGER_HOST_DISK_CHECK = crontab(minute='*/15', day_of_week="sunday")

POOL_SLB = crontab(minute='*/30', day_of_week="sunday")

POOL_GATEWAY = crontab(minute='*/30', day_of_week="sunday")

POOL_HOST = crontab(minute='*/30', day_of_week="sunday")

YODNS_REFLUSH = crontab(minute='*/20', day_of_week="sunday")
#


