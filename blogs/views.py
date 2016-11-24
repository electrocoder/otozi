#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
    """
    roket ana sayfa
    """
    return render_to_response('index.html')