from django.http import HttpResponse
from django.template import RequestContext

def index(request, extra_context = None):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)

    return HttpResponse('Woooooo!')

