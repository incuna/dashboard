from django.core.mail import mail_admins
from django.db.models import Avg, Manager

class PeriodManager(Manager):
    def last_finish(self):
        """Returns the latest Period by finish date"""
        periods = self.get_query_set().all().order_by('-finish')
        if periods:
            return periods[0]
        else:
            mail_admins('No IMC Periods of Time',
                    'The IMC app needs some attention, I\'ve created a blank one for'
                    ' now until the default time away (imc/managers.py L11)')
            return periods

class RatingManager(Manager):
    def get_rating(self, movie):
        """Return the rating for a movie"""
        rating = self.get_query_set().filter(movie=movie).aggregate(rating=Avg('rating'))['rating']
        if rating:
            current_rating = str(round(float(rating), 0))[:-2]
        else:
            current_rating = '0'
        return current_rating

