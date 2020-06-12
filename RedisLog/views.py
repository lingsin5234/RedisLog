import logging
import random as rdm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .tasks import timer_queue, azure_OCR
from .azure_blob_handler import blob_handler_test
from .oper import database_structure as ds
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

    #  ---  for testing only  ---  #
    # retrieve next available image
    query = 'SELECT container_name, image_name FROM mnl_load_receipt WHERE processed_bool=?'
    c = ds.engine.connect()
    result = c.execute(query, False).fetchall()

    # choose random result
    idx = rdm.randint(0, len(result))
    #  --------------------------  #

    # store the image to azure blob
    # azure_blob = blob_handler_test(post_details)
    # container = azure_blob['container']
    container, image_name = result[idx]
    print('INPUTS:', container, image_name)

    # run the azure OCR task
    azure_OCR.delay(container, image_name)

    return HttpResponseRedirect("/redis-queue")


# load task result
def load_result(request):

    context = {
        'results': ['result']
    }

    return render(request, 'partials/redis_queue_update.html', context)
