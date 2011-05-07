from django.contrib import admin

from forms import MovieAdminForm
from models import Movie

class MovieAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'imdb_link', 'start', 'finish', 'added_by')
    list_display = ('name', 'finish', 'added_by')
    list_filter = ('finish',)
    ordering = ('-finish',)
    prepopulated_fields = {'slug': ('name',)}

    form = MovieAdminForm

    def get_form(self, request, obj=None, **kwargs):
         form = super(MovieAdmin, self).get_form(request, obj, **kwargs)
         form.current_user = request.user
         return form

admin.site.register(Movie, MovieAdmin)

