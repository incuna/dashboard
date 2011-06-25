from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from forms import MovieRatingForm, MovieRatingInlineForm
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
            return redirect(reverse('movie-group-rating'))
    else:
        formset = MovieFormSet()

    context.update({'formset': formset, 'movie': movie, 'rating': Rating.objects.get_rating(movie=movie)})
    return render_to_response(template_name, context)

@login_required
def movie(request, slug, extra_context=None, template_name='imc/movie.html'):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)

    movie = get_object_or_404(Movie, slug=slug)
    if Rating.objects.filter(user=request.user, movie=movie):
        context.update({
            'form': MovieRatingForm,
            'rating': str(round(Rating.objects.get_rating(movie=movie)['rating'], 0))[:-2]
        })

    context.update({'movie': movie})
    return render_to_response(template_name, context)

def widget(request, extra_context = None, template_name='imc/widget.html'):
    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)
    context.update({'movie': Movie.objects.current(), 'rating': Movie.get_rating_for(movie)})
    return render_to_response(template_name, context)

