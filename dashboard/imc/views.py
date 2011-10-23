from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from forms import MovieRatingForm, MovieRatingInlineForm, MovieSubmissionForm
from models import Movie, Rating

class Current(CreateView):
    form_class = MovieRatingForm
    model = Movie
    template_name = 'imc/current.html'

    def form_valid(self, form):
        if not hasattr(self.request.user, 'profile'):
            messages.error(self.request, 'The admin cannot rate movies.')
            return redirect(reverse('index'))
        messages.info(self.request, 'Thanks for rating!')
        return super(Current, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Current, self).get_context_data(**kwargs)
        movie = Movie.objects.current()
        context['movie'] = movie
        if Rating.objects.filter(user=self.request.user, movie=movie):
            context['rating'] = Rating.objects.get_rating(movie=movie)
        return context

    def get_form(self, form_class):
        form = super(Current, self).get_form(form_class)
        form.instance.movie = Movie.objects.current()
        form.instance.user = self.request.user.profile
        return form

    def get_success_url(self):
        return reverse('movie-current')

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

class Index(TemplateView):
    template_name = 'imc/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context.update({'movie': Movie.objects.current()})
        return context

class Previous(ListView):
    template_name = 'imc/previous.html'

    def get_queryset(self):
        return Movie.objects.filter(period__finish__lt=datetime.now())

class Submit(CreateView):
    form_class = MovieSubmissionForm
    model = Movie
    template_name = 'imc/submit.html'

    def form_valid(self, form):
        form.added_by = self.request.user
        messages.info(self.request, '')
        return super(Submit, self).form_valid(form)

    def get_success_url(self):
        return reverse('movie-submit')

class Widget(DetailView):
    model = Movie
    queryset = Movie.objects.current()
    template_name = 'imc/widget.html'

    def get_context_data(self, **kwargs):
        context = super(Widget, self).get_context_data(**kwargs)
        context['rating'] = Movie.get_rating_for(self.get_queryset())
        return context

