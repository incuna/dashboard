from django.db.models import Avg, Manager

from datetime import datetime

class MovieManager(Manager):
    def current_movie(self):
        """Return the current movie"""
        current_movie = None
        try:
            current_movie = self.get_query_set().filter(finish__gt=datetime.now()).order_by('finish')[0]
        except IndexError:
            pass
        return current_movie

class RatingManager(Manager):
    def get_rating(self, movie):
        """Return the rating for a movie"""
        return self.get_query_set().filter(movie=movie).aggregate(rating=Avg('rating'))

