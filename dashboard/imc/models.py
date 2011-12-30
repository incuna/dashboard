from re import compile
from urllib2 import urlopen

from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db import models
from django.db.models import Sum
from django.template.defaultfilters import slugify
from imdb import IMDb
from profiles.models import Profile

from imc.managers import MovieManager, RatingManager

class Movie(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    added_by = models.ForeignKey(Profile)
    is_current = models.BooleanField()
    index = models.IntegerField(unique=True, null=True, blank=True)
    begin = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True,
                help_text='Defaults to %s days after start' % settings.IMC_DEFAULT_PERIOD)

    # imdb data
    imdb_id = models.CharField(max_length=7, unique=True, null=True, blank=True)
    imdb_link = models.CharField('Enter your Film\'s IMDb Link', max_length=255, blank=True)
    image = models.ImageField(upload_to='imc/covers/', null=True)
    thumbnail = models.ImageField(upload_to='imc/covers/thumbs/', null=True)
    plot = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=255, null=True, blank=True)
    writer = models.CharField(max_length=255, null=True, blank=True)
    imdb_rating = models.FloatField(null=True, blank=True)
    year = models.CharField(max_length=4, null=True, blank=True)

    objects = MovieManager()

    def __unicode__(self):
        return self.name

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
                    self._cache_image(self.image, movie['full-size cover url'], self.slug)
                    self._cache_image(self.thumbnail, movie['cover url'], self.slug, '-thumb')
                    self.plot = movie['plot outline']
                    self.imdb_rating = movie['rating']
                    self.year = movie['year']
                    self.director = ', '.join([person['name'] for person in movie['director']])
                    self.writer = ', '.join([person['name'] for person in movie['writer']])
                except KeyError:
                    pass
        return super(Movie, self).save(*args, **kwargs)

    def added_by_display(self):
        # TODO: WTF does this do?!
        return self.added_by.user.first_name

    added_by_display.short_description = 'Added By'

    # TODO: Fix this right up - looks horrid
    def get_imdb_image_url(self, movie_id):
        api = IMDb()
        movie = api.get_movie(movie_id)
        return movie['cover url']

    @staticmethod
    def make_current(movie):
        old = Movie.objects.get(is_current=True)
        old.is_current = False
        movie.is_current = True
        movie.index = old.index + 1

    @staticmethod
    def get_rating_for(movie):
        return Rating.objects.filter(movie=movie).aggregate(rating=Sum('rating'))['rating']

    @staticmethod
    def exists(imdb_id):
        try:
            return Movie.objects.get(imdb_id=imdb_id)
        except Movie.DoesNotExist:
            return None

    def _cache_image(self, field, url, slug, fn_suffix=''):
        """Store image locally"""
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(urlopen(url).read())
        img_temp.flush()
        fn = '%s%s.%s' % (slug, fn_suffix, url.rsplit('.', 1)[1])
        field.save(fn, File(img_temp), save=False)


class Rating(models.Model):
    user = models.ForeignKey(Profile)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField(max_length=2, blank=True, default=0)

    objects = RatingManager()

    class Meta:
        unique_together = ('user', 'movie')

    def __unicode__(self):
        return '%s rated %s: %s' % (self.user, self.movie.name, self.rating)

