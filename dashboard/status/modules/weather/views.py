from re import compile
from string import capwords

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from feedparser import parse

from utils import get_image_called, Weather

def index(request, extra_context = None):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)

    feed = parse(settings.BBC_HOURLY_WEATHER).entries[0]
    summary = feed.summary_detail.value.split(', ')
    summary.append(', '.join(summary[4:6]))
    del(summary[4:6])
    weather = Weather(*summary)
    weather.title = feed.title

    regex = compile(r'^.+GMT:\s+(?P<type>.*\.).+$').match(feed.title)
    if regex:
        weather_type = regex.group('type')
        for word in weather_type.split(' '):
            weather_type = weather_type.replace(word, word.capitalize())
        weather.icon = get_image_called(weather_type.strip('.'))

    upcoming = []
    for entry in parse(settings.BBC_WEEKLY_WEATHER).entries:
        match = compile(r'^.+: ([a-zA-Z ]+),').match(entry.title)
        if match:
            upcoming.append(get_image_called(capwords(match.group(1)), minimal=True))
    if upcoming:
        weather.upcoming = upcoming

    context.update({'weather': weather})
    return render_to_response('weather/index.html', context)

