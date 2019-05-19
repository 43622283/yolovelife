from celery.schedules import crontab

WORKORDER_RECORD = crontab(minute='*/2', day_of_month='27')

WORKORDER_DASHBOARD_COUNT = crontab(minute='*/20', day_of_month='27')

ORGANIZATION_SYNC = crontab(minute='*/20', day_of_month='27')