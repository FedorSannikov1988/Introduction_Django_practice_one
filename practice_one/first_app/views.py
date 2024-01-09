import logging
from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    logger.info('index page accessed, get message: Hello, world!')
    return HttpResponse("Hello, world!")
