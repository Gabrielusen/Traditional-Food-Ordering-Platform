from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    :return: main view for page templates
    """
    return HttpResponse('Hello World')
