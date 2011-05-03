from django.contrib import admin

from imc.forms import MovieChangeForm
from imc.models import Movie

class MovieAdmin(admin.ModelAdmin):
    date_hierarchy = 'view_by'
    exclude = ('imdb_id', 'thumbnail', 'image', 'plot', 'imdb_rating', 'year', 'director', 'writer')
    list_display = ('name', 'view_by', 'added_by_display')
    list_filter = ('view_by',)
    ordering = ('view_by',)

    form = MovieChangeForm

admin.site.register(Movie, MovieAdmin)

