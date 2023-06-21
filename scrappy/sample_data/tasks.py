import time

from datetime import datetime
from celery import shared_task


@shared_task
def wait(seconds: int):
    time.sleep(seconds)
    return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
