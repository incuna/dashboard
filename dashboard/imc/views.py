from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from imc.forms import MovieRatingForm
from imc.models import FilmBuff, Movie

def index(request, extra_context = None):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)
    context.update({'movie': Movie.objects.current_movie()})
    return render_to_response('imc/index.html', context)

@login_required
def movie(request, extra_context = None):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)

    movie = Movie.objects.current_movie()
    if request.method == 'POST':
        form = MovieRatingForm(request.POST)
        if form.is_valid():
            # add the rating value the user has chosen to the movie's overall rating
            instance = form.save(commit=False)
            instance.movie = movie
            #instance.user = request.user
            instance.user = FilmBuff.objects.get(username='george')
            instance.save()
            return redirect(reverse('movie'))
    else:
        form = MovieRatingForm()

    context.update({'form': form, 'movie': movie, 'users': FilmBuff.objects.all().order_by('username')})
    return render_to_response('imc/movie.html', context)

