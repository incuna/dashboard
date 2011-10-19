from django.forms.widgets import RadioSelect
from django import forms
from incuna.forms.widgets import DateWidget, ReadOnlyWidget
from django.conf import settings

from models import Holiday, HolidayRequest

class HolidayForm(forms.ModelForm):
    date = forms.DateField(widget=ReadOnlyWidget)
    class Meta:
        model = Holiday
        exclude = ('holiday_request',)
    
class HolidaySelectionForm(forms.ModelForm):
    start_date = forms.DateField(widget=DateWidget(format=settings.DATE_FORMAT), input_formats=settings.DATE_INPUT_FORMATS, help_text='The first day of holiday.')
    days_off = forms.IntegerField(min_value=1,max_value=30, help_text='The number of weekdays to request.')
    class Meta:
        model = HolidayRequest
        fields = ('employee_comment',)

    def __init__(self, *args, **kwargs):
        super(HolidaySelectionForm, self).__init__(*args, **kwargs)

        keyOrder = list(self._meta.fields)
        keyOrder[0:0]= ['start_date', 'days_off']
        self.fields.keyOrder = keyOrder

class HolidayRequestAuthForm(forms.ModelForm):
    STATUS_CHOICES = ((1,'Accept'),
                      (2,'Deny'))
    status = forms.TypedChoiceField(widget=RadioSelect,choices=STATUS_CHOICES, coerce=int)
    class Meta:
        model = HolidayRequest
        fields = ('status','manager_comment')

class HolidayComment(forms.Form):
    comment = forms.CharField(widget=ReadOnlyWidget, max_length=255, required=False)
