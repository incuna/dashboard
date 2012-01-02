from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, FormView, ListView, TemplateView

from imc.forms import RatingForm, RatingFormSet, SelectForm, SubmissionForm
from imc.models import Movie, Rating
from utils import class_view_decorator

@class_view_decorator(login_required)
class Current(CreateView):
    form_class = RatingForm
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


@class_view_decorator(login_required)
class GroupRating(CreateView):
    formset_class = RatingFormSet
    template_name = 'imc/group_rating.html'
    queryset = Rating.objects.none()

    def formset_valid(self, formset):
        for obj in formset.save(commit=False):
            obj.movie = self.movie
            obj.save()
        return redirect(self.get_success_url())

    def formset_invalid(self, formset):
        return self.render_to_response(self.get_context_data(formset=formset))

    def get_context_data(self, **kwargs):
        context = super(GroupRating, self).get_context_data(**kwargs)
        context['movie'] = Movie.objects.current()
        context['formset'] = self.formset_class()
        return context

    def post(self, request, *args, **kwargs):
        formset = self.formset_class(request.POST)
        if formset.is_valid():
            return self.formset_valid(formset)
        return self.formset_invalid(formset)

    def get_success_url(self):
        return reverse('movie-group-rating')


@class_view_decorator(login_required)
class Index(TemplateView):
    template_name = 'imc/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context.update({'movie': Movie.objects.current()})
        return context


@class_view_decorator(login_required)
class Pool(ListView):
    queryset = Movie.objects.filter(index__isnull=True)
    template_name = 'imc/pool.html'


@class_view_decorator(login_required)
class Previous(ListView):
    queryset = Movie.objects.filter(index__isnull=False)
    template_name = 'imc/previous.html'


@class_view_decorator(login_required)
class Select(FormView):
    form_class = SelectForm

    def get_initial(self):
        # TODO: add the game theory to get a random movie here.
        # TODO: the actual code needs to go on the model as a static method
        # TODO: Can probably get away with putting this on the initial var if it's just a function
        pass

    def get_success_url(self):
        return reverse('movie-index')


@class_view_decorator(login_required)
class Submit(CreateView):
    form_class = SubmissionForm
    model = Movie
    template_name = 'imc/submit.html'

    def form_valid(self, form):
        new_film = form.save(commit=False)
        new_film.added_by = self.request.user.profile
        new_film.save()
        messages.info(self.request, '%s has been added to the movie pool.' % new_film.name)
        return super(Submit, self).form_valid(form)

    def get_success_url(self):
        return reverse('movie-submit')


@class_view_decorator(login_required)
class Widget(DetailView):
    model = Movie
    queryset = Movie.objects.current()
    template_name = 'imc/widget.html'

    def get_context_data(self, **kwargs):
        context = super(Widget, self).get_context_data(**kwargs)
        context['rating'] = Movie.get_rating_for(self.get_queryset())
        return context

