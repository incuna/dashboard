from django.contrib import admin

from forms import MovieAdminForm
from models import Movie

class MovieAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'imdb_link', 'start', 'finish', 'added_by']
    list_display = ['name', 'finish', 'added_by']
    list_filter = ('finish',)
    ordering = ('-finish',)
    prepopulated_fields = {'slug': ('name',)}

    form = MovieAdminForm

    def get_form(self, request, obj=None, **kwargs):
        current_user = request.user
        if not current_user.is_superuser and not current_user.profile.is_manager:
            self.fields.remove('added_by')
            self.list_display.remove('added_by')
        form = super(MovieAdmin, self).get_form(request, obj, **kwargs)
        form.current_user = current_user
        return form

    def queryset(self, request):
        user = getattr(request, 'user', None)
        qs = super(MovieAdmin, self).queryset(request)
        if user.is_superuser or user.profile.is_manager:
            return qs
        return qs.filter(added_by=user)

admin.site.register(Movie, MovieAdmin)

