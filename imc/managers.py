from django.db.models import Avg, Manager

class MovieManager(Manager):
    def current(self):
        movie_by_index = self.get_query_set().filter(index__isnull=False).order_by('-index')
        try:
            return movie_by_index[0]
        except IndexError:
            return None


class RatingManager(Manager):
    def get_rating(self, movie):
        """Return the rating for a movie"""
        rating = self.get_query_set().filter(movie=movie).aggregate(rating=Avg('rating'))['rating']
        if rating:
            current_rating = str(round(float(rating), 0))[:-2]
        else:
            current_rating = '0'
        return current_rating

