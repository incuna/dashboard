from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from forms import MovieRatingForm
from models import Movie, Rating

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
            instance = form.save(commit=False)
            instance.movie = movie
            instance.user = request.user
            instance.save()
            return redirect(reverse('movie'))
    else:
        form = MovieRatingForm()
        if Rating.objects.filter(user=request.user, movie=movie):
            context.update({'rating': Rating.objects.get_rating(movie=movie)['rating']})

    context.update({'form': form, 'movie': movie, 'user': request.user})
    return render_to_response('imc/movie.html', context)

