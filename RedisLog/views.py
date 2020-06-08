import logging

from django.shortcuts import render
from django.http import HttpResponse

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)


def index(request):
    # Send the Test!! log message to standard out
    logger.error("Test!!")
    return HttpResponse("Hello logging world.")
