from celery.schedules import crontab
#
DASHBOARD_STATS_COUNT = crontab(hour="*", day_of_week="Friday")

DASHBOARD_STATS_WORK = crontab(minute="*/30", day_of_week="Friday")

DASHBOARD_STATS_GROUP = crontab(minute="*/30", day_of_week="Friday")

DASHBOARD_GROUP_LOAD = crontab(minute="*", day_of_week="Friday")

DASHBOARD_EXPIRED_TIME = crontab(minute="*", day_of_week="Friday")

MANAGER_HOST_TIME = crontab(minute='*/30', day_of_week="Friday")

MANAGER_HOST_SSH_CHECK = crontab(minute='*/10', day_of_week="Friday")

MANAGER_HOST_LOAD_CHECK = crontab(minute='*/30', day_of_week="Friday")

MANAGER_HOST_DISK_CHECK = crontab(minute='*/15', day_of_week="Friday")

MANAGER_PASSWORD_CHECK = crontab(minute='11', hour='3', day_of_week="Friday")

# MANAGER_PASSWORD_CHANGE = crontab(minute='*')
MANAGER_PASSWORD_CHANGE = crontab(minute='11', hour='3', day_of_month='29', day_of_week="Friday")

POOL_SLB = crontab(minute='*/30', day_of_week="Friday")

POOL_GATEWAY = crontab(minute='*/30', day_of_week="Friday")

POOL_HOST = crontab(minute='*/30', day_of_week="Friday")

YODNS_REFLUSH = crontab(minute='*/20', day_of_week="Friday")

ZDB_INSTANCE_FLUSH = crontab(minute='*/10', day_of_week="Friday")

ZDB_DATABASE_FLUSH = crontab(minute='*/10', day_of_week="Friday")

WORKORDER_RECORD = crontab(minute='*', day_of_week="Tuesday")

WORKORDER_DASHBOARD_COUNT = crontab(minute='*/10', day_of_week="Friday")

WORKORDER_DASHBOARD_REPOSITORY = crontab(minute='*/30', day_of_week="Friday")

WORKORDER_REPORT_DAY = crontab(minute='*/30', day_of_week="Friday")

WORKORDER_REPORT_WEEK = crontab(minute='*/30', day_of_week="Friday")

WORKORDER_REPORT_MONTH = crontab(minute='*/30', day_of_week="Friday")

