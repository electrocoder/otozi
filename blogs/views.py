#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from forms import *
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from eventregistry import *

def index(request):
    """
    roket ana sayfa
    """
    return render_to_response('index.html')

@csrf_protect
@csrf_exempt
def eventregistry(request):
    """
    """
    if request.method=='POST':
        form = QForm(request.POST)
        if form.is_valid():
            er = EventRegistry()
            q = QueryEvents()
            q.addConcept(er.getConceptUri(request.POST['q']))
            q.addRequestedResult(RequestEventsInfo(sortBy="date", count=2))  # return event details for last 10 events
            val = er.execQuery(q)
            return render(request, 'eventregistry.html', locals())
        else:
            val = "istek yanlis"

    return render(request, 'eventregistry.html', locals())





