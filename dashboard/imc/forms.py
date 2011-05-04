from django import forms
from django.forms import RadioSelect
from django.forms.widgets import flatatt, RadioFieldRenderer, RadioInput
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

from models import Movie, UserRating

class MovieAdminForm(forms.ModelForm):

    class Meta:
        model = Movie

    def save(self, commit=False):
        instance = super(MovieAdminForm, self).save(commit=commit)
        instance.added_by = self.current_user.filmbuff
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
        return mark_safe(u'%s' % self.tag())

    def tag(self):
        if 'id' in self.attrs:
            self.attrs['id'] = '%s_%s' % (self.attrs['id'], self.index)
        final_attrs = dict(self.attrs, type='radio', name=self.name, value=self.choice_value, title=self.choice_title)
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

class MovieRatingForm(forms.ModelForm):
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
    rating = forms.ChoiceField(choices=RATING_CHOICES, required=True,
            widget=RadioSelect(renderer=InputOnlyRadioRenderer))

    class Meta:
        model = UserRating
        fields = ('rating',)

