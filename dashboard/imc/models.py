from datetime import datetime
from re import compile

from django.db import models
from django.contrib.auth.models import User
from imdb import IMDb

class FilmBuff(models.Model):
    user = models.OneToOneField(User)
    is_film_buff = models.BooleanField()

    def __unicode__(self):
        return self.user.get_fullname()

class MovieManager(models.Manager):
    def current_movie(self):
        """Return the current movie"""
        current_movie = None
        try:
            current_movie = self.get_query_set().filter(view_by__gt=datetime.now()).order_by('finish')[0]
        except IndexError:
            pass
        return current_movie

class Movie(models.Model):
    name = models.CharField(max_length=255)
    start = models.DateField()
    finish = models.DateField()
    added_by = models.ForeignKey(FilmBuff)

    # imdb data
    imdb_id = models.CharField(max_length=7, null=True, blank=True)
    imdb_link = models.CharField('IMDb Link', max_length=255, blank=False)
    thumbnail = models.CharField(max_length=255, null=True)
    image = models.CharField(max_length=255, null=True)
    plot = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=255, null=True, blank=True)
    writer = models.CharField(max_length=255, null=True, blank=True)
    imdb_rating = models.FloatField(null=True, blank=True)
    year = models.CharField(max_length=4, null=True, blank=True)

    objects = MovieManager()

    def __unicode__(self):
        return self.name

    def added_by_display(self):
        return self.added_by.user.first_name

    added_by_display.short_description = 'Added By'

    def get_imdb_image_url(self, movie_id):
        api = IMDb()
        movie = api.get_movie(movie_id)
        return movie['cover url']

    def save(self, *args, **kwargs):
        matches = compile(r'^(http://)?(www\.)?imdb\.com/title/tt(\d+)').match(self.imdb_link)
        if matches and matches.group(3):
            api = IMDb()
            movie = api.get_movie(matches.group(3))
            self.imdb_id = movie.movieID
            try:
                self.thumbnail = movie['cover url']
                self.image = movie['full-size cover url']
                self.plot = movie['plot outline']
                self.imdb_rating = movie['rating']
                self.year = movie['year']
                self.director = join_person_list(movie['director'])
                self.writer = join_person_list(movie['writer'])
            except KeyError:
                pass
        return super(Movie, self).save(*args, **kwargs)

class UserRating(models.Model):
    user = models.ForeignKey(FilmBuff)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField(max_length=2, blank=True, default=0)

    def __unicode__(self):
        return '%s rated %s: %s' % (self.user, self.movie.name, self.rating)

def join_person_list(persons):
    person_list = []
    for person in persons:
        person_list.append(person['name'])
    return ', '.join(person_list)

