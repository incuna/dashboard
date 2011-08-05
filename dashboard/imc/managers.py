from django.core.mail import mail_admins
from django.db.models import Avg, Manager
from django.http import HttpResponseRedirect

class PeriodManager(Manager):
    def last_finish(self):
        """Returns the latest Period by finish date"""
        try:
            self.get_query_set().all().order_by('-finish')[0]
        except IndexError:
            mail_admins('No IMC Periods of Time',
                    'The IMC app needs you to create some Periods of Time! (imc/managers.py L11)')
            return HttpResponseRedirect('/')


class RatingManager(Manager):
    def get_rating(self, movie):
        """Return the rating for a movie"""
        rating = self.get_query_set().filter(movie=movie).aggregate(rating=Avg('rating'))['rating']
        if rating:
            current_rating = str(round(float(rating), 0))[:-2]
        else:
            current_rating = '0'
        return current_rating

