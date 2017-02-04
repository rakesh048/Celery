from datetime import timedelta
from celery.decorators import periodic_task
from celery_app.views import celery_function
from celery.utils.log import get_task_logger

 
@periodic_task(run_every=timedelta(seconds=5))
def scraper_example():
    celery_function()


# this work go in setting.py file and set TIME_ZONE = 'Asia/Kolkata'
# @periodic_task(run_every=crontab(hour=7, minute=30, day_of_week="mon"))
# def every_monday_morning():
#     print("This runs every Monday morning at 7:30a.m.")



