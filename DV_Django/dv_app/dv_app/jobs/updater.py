from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import update_estan
from pytz import utc

job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

def start():
    scheduler = BackgroundScheduler(job_defaults=job_defaults, timezone=utc)
    scheduler.add_job(update_estan, 'interval', seconds=28800)
    scheduler.start()

# def start():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(update_estan, 'cron', hour=21, minute=9)
#     scheduler.start()