from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.views.generic import ListView

from forms import MovieRatingForm, MovieRatingInlineForm, MovieSubmissionForm
from models import Movie, Rating

@login_required
def current(request, extra_context=None, template_name='imc/current.html'):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)

    movie = Movie.objects.current()
    if request.method == 'POST':
        form = MovieRatingForm(request.POST)
        if form.is_valid():
            if not hasattr(request.user, 'profile'):
                messages.error(request, 'The admin cannot rate movies.')
                return redirect(reverse('index'))
            instance = form.save(commit=False)
            instance.movie = movie
            instance.user = request.user.profile
            instance.save()
            return redirect(reverse('movie-current'))
    else:
        form = MovieRatingForm()
        if Rating.objects.filter(user=request.user, movie=movie):
            context.update({'rating': Rating.objects.get_rating(movie=movie)})

    context.update({'form': form, 'movie': movie, 'user': request.user})
    return render_to_response(template_name, context)

@login_required
def group_rating(request, slug=None, extra_context=None, template_name='imc/group_rating.html'):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)

    movie = Movie.objects.current()
    MovieFormSet = inlineformset_factory(Movie, Rating, form=MovieRatingInlineForm)
    if request.method == 'POST':
        formset = MovieFormSet(request.POST, instance=movie)
        if formset.is_valid():
            formset.save()
            return redirect(reverse('movie-index'))
    else:
        formset = MovieFormSet()

    context.update({'formset': formset, 'movie': movie, 'rating': Rating.objects.get_rating(movie=movie)})
    return render_to_response(template_name, context)

@login_required
def index(request, extra_context=None, template_name='imc/index.html'):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)
    context.update({'movie': Movie.objects.current()})
    return render_to_response(template_name, context)

@login_required
def movie(request, slug, extra_context=None, template_name='imc/movie.html'):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)
    movie = get_object_or_404(Movie, slug=slug)
    context.update({'movie': movie, 'rating': Rating.objects.get_rating(movie=movie)})
    return render_to_response(template_name, context)

class PreviousMovieListView(ListView):
    template_name = 'imc/previous.html'

    def get_queryset(self):
        return Movie.objects.filter(period__finish__lt=datetime.now())

@login_required
def submit(request, extra_context=None, template_name='imc/submit.html'):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)
    if request.method == 'POST':
        form = MovieSubmissionForm(request.POST)
        if form.is_valid():
            new_film = form.save(commit=False)
            new_film.added_by = request.user.profile
            new_film.save()
            return HttpResponseRedirect(reverse('movie-index'))
    else:
        form = MovieSubmissionForm()

    context.update({'form': form})
    return render_to_response(template_name, context)

def widget(request, extra_context = None, template_name='imc/widget.html'):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)
    context.update({'movie': Movie.objects.current(), 'rating': Movie.get_rating_for(movie)})
    return render_to_response(template_name, context)

