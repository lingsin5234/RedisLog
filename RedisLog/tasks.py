from django_rq import job
import time as t


@job
def timer_queue():
    t.sleep(60)  # sleep 60 seconds
