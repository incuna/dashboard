from re import compile

from django import forms
from django.forms import RadioSelect
from django.forms.models import modelformset_factory
from django.forms.widgets import flatatt, RadioFieldRenderer, RadioInput
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from profiles.models import Profile

from imc.models import Movie, Rating

class MovieAdminForm(forms.ModelForm):

    class Meta:
        model = Movie

    def save(self, commit=False):
        instance = super(MovieAdminForm, self).save(commit=commit)
        if not instance.pk and not self.current_user.is_superuser:
            if not self.current_user.profile.is_manager:
                instance.added_by = self.current_user.profile
        instance.save()
        return instance

class InputOnlyRadioInput(RadioInput):
    """
    An object used by InputOnlyRadioFieldRenderer that represents a single
    <input type='radio'> without a <label> tag.
    """

    def __init__(self, name, value, attrs, choice, index):
        self.name, self.value = name, value
        self.attrs = attrs
        self.choice_value = force_unicode(choice[0])
        self.choice_title = force_unicode(choice[1])
        self.index = index

    def __unicode__(self):
        return mark_safe(self.tag())

    def tag(self):
        if 'id' in self.attrs:
            self.attrs['id'] = 'rating_%s' % self.index
        final_attrs = dict(self.attrs, type='radio', name=self.name, value=self.choice_value)
        if self.is_checked():
            final_attrs['checked'] = 'checked'
        return mark_safe(u'<input%s>' % flatatt(final_attrs))

class InputOnlyRadioRenderer(RadioFieldRenderer):
    """
    This overrides the default radio button widget renderer method to
    output radio buttons inputs with no extra tags.
    """
    def __init__(self, name, value, attrs, choices):
        self.name, self.value, self.attrs = name, value, attrs
        self.choices = choices

    def __iter__(self):
        for i, choice in enumerate(self.choices):
            yield InputOnlyRadioInput(self.name, self.value, self.attrs.copy(), choice, i)

    def __getitem__(self, idx):
        choice = self.choices[idx] # Let the IndexError propogate
        return InputOnlyRadioInput(self.name, self.value, self.attrs.copy(), choice, idx)

    def render(self):
        """Outputs radios"""
        return mark_safe(u'%s' % u'\n'.join([u'%s\n' % force_unicode(w) for w in self]))

RATING_CHOICES = (
    (1, 'Very Poor'),
    (2, 'Poor'),
    (3, 'Not That Bad'),
    (4, 'Fair'),
    (5, 'Average'),
    (6, 'Almost Good'),
    (7, 'Good'),
    (8, 'Very Good'),
    (9, 'Excellent'),
    (10, 'Perfect'),
)
class BaseRatingForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=RATING_CHOICES, required=True,
            widget=RadioSelect(renderer=InputOnlyRadioRenderer))

    class Meta:
        abstract = True
        model = Rating


class RatingForm(BaseRatingForm):
    class Meta(BaseRatingForm.Meta):
        fields = ('rating',)


current_movie_ratings = Rating.objects.filter(movie=Movie.objects.current()).values('user')
not_yet_rated = Profile.objects.exclude(id__in=current_movie_ratings)
class GroupRatingForm(BaseRatingForm):
    user = forms.ModelChoiceField(queryset=not_yet_rated)

    class Meta(BaseRatingForm.Meta):
        exclude = ('movie',)

RatingFormSet = modelformset_factory(Rating, form=GroupRatingForm, extra=3)


class SelectForm(forms.ModelForm):
    pass

class SubmissionForm(forms.ModelForm):

    class Meta:
        fields = ('imdb_link',)
        model = Movie

    def clean(self, *args, **kwargs):
        cleaned_data = super(SubmissionForm, self).clean(*args, **kwargs)
        movie = Movie.exists(compile(r'.+\/tt(\d+)\/').match(cleaned_data['imdb_link']).group(1))
        if movie:
            raise forms.ValidationError('%s has already submitted this movie' %
                                        movie.added_by.first_name.capitalize())
        return cleaned_data

