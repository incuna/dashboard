from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Item

def index(request, extra_context = None):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)

    context.update({'shoppinglist': Item.objects.filter(bought=False).order_by('-created')})
    return render_to_response('shoppinglist/index.html', context)

