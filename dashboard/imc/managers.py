from datetime import datetime

from django.db.models import Avg, Manager

class MovieManager(Manager):
    def current(self):
        """Return the current movie"""
        try:
            return self.get_query_set().filter(finish__gte=datetime.now()).order_by('finish')[0]
        except IndexError:
            raise self.model.DoesNotExist

class RatingManager(Manager):
    def get_rating(self, movie):
        """Return the rating for a movie"""
        rating = self.get_query_set().filter(movie=movie).aggregate(rating=Avg('rating'))['rating']
        if rating:
            current_rating = str(round(float(rating), 0))[:-2]
        else:
            current_rating = '0'
        return current_rating

