from django.http import HttpResponse

def index(request, extra_context = None):
    return HttpResponse('index')
