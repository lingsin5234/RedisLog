import logging

from django.shortcuts import render
from django.http import HttpResponse
from .tasks import timer_queue

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)


def index(request):
    # Send the Test!! log message to standard out
    # logger.error("Test!!")

    # run the queue job
    timer_queue.delay()

    return HttpResponse("Hello logging world.")


# redis queue
def view_redis_queue(request):

    context = {

    }

    return render(request, 'pages/redis_queue.html', context)


# load task result
def load_result(request):

    context = {

    }

    return render(request, 'partials/redis_queue_update.html', context)
