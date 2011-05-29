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
        if not request.user.is_superuser:
            if not request.user.profile.is_manager:
                self.exclude = ('added_by',)
        form.current_user = request.user
        return form

    def queryset(self, request):
        user = getattr(request, 'user', None)
        qs = super(MovieAdmin, self).queryset(request)
        if user.is_superuser or user.profile.is_manager:
            return qs
        return qs.filter(added_by=user)

admin.site.register(Movie, MovieAdmin)

