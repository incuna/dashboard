from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Item

def index(request, extra_context = None):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)

    items = Item.objects.filter(bought=False).order_by('created')
    more = None
    if items.count() > 9:
        more = items.count() - 8
        items = items[:8]

    context.update({'items': items, 'more': more})
    return render_to_response('shoppinglist/index.html', context)

