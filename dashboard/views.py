from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request, extra_context = None):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)

    return render_to_response('index.html', context)

