import time
from celery import shared_task


@shared_task
def process_url(url):
    time.sleep(10)
    return time.time()
