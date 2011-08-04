from django.db.models import Avg, Manager

class PeriodManager(Manager):
    def last_finish(self):
        """Returns the latest Period by finish date"""
        return self.get_query_set().all().order_by('-finish')[0]

class RatingManager(Manager):
    def get_rating(self, movie):
        """Return the rating for a movie"""
        rating = self.get_query_set().filter(movie=movie).aggregate(rating=Avg('rating'))['rating']
        if rating:
            current_rating = str(round(float(rating), 0))[:-2]
        else:
            current_rating = '0'
        return current_rating

