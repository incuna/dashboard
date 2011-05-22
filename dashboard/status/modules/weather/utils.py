# coding=utf8
from os.path import exists, join
from re import compile

from django.core.mail import mail_managers
from django.conf import settings

def get_image_called(name, minimal=False):
    """
    Get the image based on the weather type from the BBC feed.
    The images list is a mapping to the numbered images.
    """
    images = [
        'Clear Sky',
        'Sunny',
        'Partly Cloudy',
        'Sunny Intervals',
        '',
        'Mist',#5
        'Fog',
        'White Cloud',
        'Grey Cloud',
        '',
        'Light Rain Shower',#10
        'Drizzle',
        'Light Rain',
        'Heavy Rain Shower',
        '',
        'Heavy Rain',#15
        'Sleet Shower',
        '',
        'Sleet',
        '',
        '',#20
        '',
        '',
        '',
        'Light Snow',
        '',#25
        '',
        'Heavy Snow',
        '',
        '',
        '',#30
        '',
        '',
    ]
    try:
        image = '%s%s' % (images.index(name), '.png')
        path = 'images/status/weather/'
        if minimal:
            path = join(path, 'minimal')
        file_path = join(settings.STATIC_ROOT, path)
        if exists(join(file_path, image)):
            return join(settings.STATIC_URL, path, image)
        else:
            # mail_managers('Missing image file for: %s' % name, 'The file for weather image %s is needed today and isn\'t in the list, go grab it quick!' % name)
            print 'Missing image file for: %s' % name
            return None
    except ValueError:
        print '\"%s\" not found' % name
        # mail_managers('Missing image for: %s' % name, 'The weather image %s is needed today and isn\'t in the list, go grab it quick!' % name)

class Weather(object):
    centigrade = None
    farenheit = None
    icon = None
    title = None
    upcoming = None

    def __init__(self, *args):
        """args comes from the feed summary - a split string 6°C (43°F)"""
        pattern = r'^Temperature:\s(?P<centigrade>\d{1,2}).{1}C.+\((?P<farenheit>\d{1,2}).{1}F\)$'
        matched = compile(pattern).match(unicode(args[0]))
        if matched:
            self.centigrade = matched.group('centigrade')
            self.farenheit = matched.group('farenheit')
        self.w_direction = compile(r'Wind Direction: ([NESW]{1,3})').match(args[1]).group(1)
        self.w_speed = args[2][-5:-3]
        self.rel_humidity = args[3][-3:-1]
        self.visibility = args[4].replace('Visibility: ', '')
        self.pressure = args[5].replace('Pressure: ', '')

    def __repr__(self):
        return u'%s' % self.temp

