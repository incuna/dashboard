from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

@login_required
def index(request, extra_context = None):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)

    return render_to_response('index.html', context)

