from base64 import encodestring
from datetime import date
from urllib2 import Request, urlopen

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from json import loads
from profiles.models import Profile

def index(request, extra_context = None):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)
    return render_to_response('status/index.html', context)

def todays_holidays(request, extra_context = None):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)

    url = '%s/api/employees-on-holiday' % settings.HOLIDAYCAL_URL

    request = Request(url)
    base64string = encodestring('%s:%s' % ('api', 'n5fz7}|eUD^4b2<j'))[:-1]
    #base64string = encodestring('%s:%s' % ('george', '%dqn3Ura3[;Z<88J'))[:-1]
    authheader = 'Basic %s' % base64string
    request.add_header('Authorization', authheader)
    try:
        handle = urlopen(request)
        employees = loads(handle.read())['today']
    except IOError:
        print 'API Username/Password Incorrect'
        employees = None

    for i, employee in enumerate(employees):
        try:
            em = Profile.objects.get(email=employee['email'])
            employees[i]['avatar'] = str(em.avatar)
        except Profile.DoesNotExist:
            print 'Cannot find Employee: %s' % employee['username']
    context.update({'employees': employees, 'today': date.today()})

    return render_to_response('status/todays_holidays.html', context)

