import logging

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .tasks import timer_queue, azure_OCR
from .azure_blob_handler import blob_handler_test
import requests as req
import json

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

    if request.method == 'POST':
        a_msg = 'POST Requested'
    else:
        a_msg = ''

    context = {
        'message': a_msg
    }

    return render(request, 'pages/redis_queue.html', context)


# ocr submit request
def submit_ocr_request(request):

    # get request.POST details
    '''
    post_details = {
        'username': request.POST['username'],
        'image_name': request.POST['image_name'],
        'image_string': request.POST['image_string'],
    }
    '''

    # store the image to azure blob
    # azure_blob = blob_handler_test(post_details)
    # container = azure_blob['container']
    container = 'https://blobstorage005234.blob.core.windows.net/quickstartf307c613-1e65-4bb2-8e8a-4fd731cd0cdb'

    # run the azure OCR task
    azure_OCR.delay(container)

    return HttpResponseRedirect("/redis-queue")


# load task result
def load_result(request):

    context = {
        'results': ['result']
    }

    return render(request, 'partials/redis_queue_update.html', context)
