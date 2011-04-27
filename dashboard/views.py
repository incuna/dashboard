from django.shortcuts import render_to_response

def index(request, extra_context = None):
    return render_to_response('index.html')
