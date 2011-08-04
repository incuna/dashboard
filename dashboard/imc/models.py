from datetime import timedelta, datetime
from random import choice
from re import compile

from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.template.defaultfilters import slugify
from imdb import IMDb
from profiles.models import Profile

from managers import PeriodManager, RatingManager

class MovieManager(models.Manager):
    def current(self):
        try:
            return self.get_query_set().filter(period__finish__gte=datetime.now()).order_by('period__finish')[0]
        except IndexError:
            last_day = Period.objects.last_finish()
            new_period = Period.objects.create(start=last_day.finish + timedelta(7 - last_day.finish.weekday()))
            random_movie = choice(Movie.objects.unwatched())
            random_movie.period = new_period
            random_movie.save(imdb_update=False)
            return random_movie

    def previous(self):
        """Return previously selected movies"""
        return self.get_query_set().filter(finish__lt=datetime.now())

    def unwatched(self):
        """Return movies that aren't in a showing which has been watched"""
        return self.get_query_set().filter()

class Movie(models.Model):
    period = models.OneToOneField('Period', null=True, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    added_by = models.ForeignKey(Profile)

    # imdb data
    imdb_id = models.CharField(max_length=7, null=True, blank=True)
    imdb_link = models.CharField('Enter your Film\'s IMDb Link', max_length=255, blank=True)
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
        # TODO: WTF does this do?!
        return self.added_by.user.first_name

    added_by_display.short_description = 'Added By'

    # TODO: Fix this right up - looks horrid
    def get_imdb_image_url(self, movie_id):
        api = IMDb()
        movie = api.get_movie(movie_id)
        return movie['cover url']

    def save(self, imdb_update=True, *args, **kwargs):
        if imdb_update:
            matches = compile(r'^(http://)?(www\.)?imdb\.com/title/tt(\d+)').match(self.imdb_link)
            if matches and matches.group(3):
                api = IMDb()
                movie = api.get_movie(matches.group(3))
                self.name = movie['title']
                self.slug = slugify(movie['title'])
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

    @staticmethod
    def get_rating_for(movie):
        return Rating.objects.filter(movie=movie).aggregate(rating=Sum('rating'))['rating']

class Period(models.Model):
    start = models.DateField()
    finish = models.DateField(blank=True, help_text='Defaults to %s days after start' % settings.IMC_DEFAULT_PERIOD)

    objects = PeriodManager()

    class Meta:
        unique_together = ('start', 'finish')

    def __unicode__(self):
        return '%s to %s' % (self.start, self.finish)

    def save(self, *args, **kwargs):
        if not self.finish:
            self.finish = self.start + timedelta(days=settings.IMC_DEFAULT_PERIOD)
        super(Period, self).save(*args, **kwargs)

class Rating(models.Model):
    user = models.ForeignKey(Profile)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField(max_length=2, blank=True, default=0)

    objects = RatingManager()

    class Meta:
        unique_together = ('user', 'movie')

    def __unicode__(self):
        return '%s rated %s: %s' % (self.user, self.movie.name, self.rating)

def join_person_list(persons):
    person_list = []
    for person in persons:
        person_list.append(person['name'])
    return ', '.join(person_list)

