import datetime

from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms.formsets import formset_factory
from incuna.utils import class_view_decorator
from django.views.generic import ListView, TemplateView, RedirectView


from holiday.models import HolidayRequest, BankHoliday
from holiday.forms import HolidayForm, HolidaySelectionForm, HolidayRequestAuthForm, HolidayComment
from profiles.models import Profile


# for use with all the @user_passes_test stuff below
def is_manager(user):
    return user.get_profile().is_manager


@class_view_decorator(login_required)
class HomeView(RedirectView):
    def get_redirect_url(self, **kwargs):
        username = self.request.user.username
        return reverse('holiday_user', kwargs={'username': username})


@login_required
def make_holiday_request(request):
    def get_holidays(start_date, days_off):
        days = []
        one_day = datetime.timedelta(days=1)
        current = start_date
        bank_holidays = [h.date for h in BankHoliday.objects.filter(date__gte=start_date)]
        while len(days) < days_off:
            if current.weekday() < 5 and current not in bank_holidays:
                days.append({'date': current})
            current += one_day
        return days

    HolidayFormSet = formset_factory(HolidayForm, extra=0)
    context = RequestContext(request)

    # STAGE 2: first form submitted
    if request.POST:
        # STAGE 3: show confirmation
        if 'form-INITIAL_FORMS' not in request.POST:
            hol_sel_form = HolidaySelectionForm(request.POST)

            if hol_sel_form.is_valid():
                #holidays
                initial_data = get_holidays(hol_sel_form.cleaned_data['start_date'], hol_sel_form.cleaned_data['days_off'])
                form_set = HolidayFormSet(initial=initial_data)
                context['form_set'] = form_set
                #holiday request (comment)
                comment_form = HolidayComment(initial={'comment': hol_sel_form.cleaned_data['employee_comment']})
                context['comment_form'] = comment_form
            else:
                context.update({'hol_sel_form': hol_sel_form})
        # STAGE 4: accept confirmation
        else:
            form_set = HolidayFormSet(request.POST)
            comment_form = HolidayComment(request.POST)
            context['form_set'] = form_set
            if form_set.is_valid() and comment_form.is_valid():
                holiday_request = HolidayRequest(employee=request.user)
                holiday_request.employee_comment = comment_form.cleaned_data['comment']
                holiday_request.save()
                for form in form_set.forms:
                    instance = form.save(commit=False)
                    instance.holiday_request = holiday_request
                    instance.save()
                holiday_request.send_request_email()
                return HttpResponseRedirect(reverse('holiday_user', kwargs={'username': request.user.username}))
    # STAGE 1: initial form
    else:
        hol_sel_form = HolidaySelectionForm()
        context.update({'hol_sel_form': hol_sel_form})
    return render_to_response('holiday/make_request.html', context)


@class_view_decorator(login_required)
class EmployeeRequestsList(ListView):
    model = HolidayRequest
    template_name = 'holiday/view_status.html'

    def get(self, *args, **kwargs):
        self.employee = self.get_employee()
        return super(EmployeeRequestsList, self).get(*args, **kwargs)

    def get_employee(self):
        employee = get_object_or_404(Profile, username=self.kwargs['username'])
        profile = self.request.user.get_profile()
        if profile.is_manager == False and profile != employee:
            raise Http404('User does not have access')
        return employee

    def get_queryset(self):
        qs = super(EmployeeRequestsList, self).get_queryset()
        return qs.filter(
            employee__pk=self.employee.pk,
            holiday__date__year=datetime.datetime.now().year
        ).order_by('-start_date')

    def get_context_data(self, **kwargs):
        kwargs['employee'] = self.employee
        return super(EmployeeRequestsList, self).get_context_data(**kwargs)


@login_required
def request_details(request, pk):
    qs = HolidayRequest.objects.all()
    context = RequestContext(request)
    #if user is staff , ensure this is one of their requests
    profile = request.user.get_profile()
    if not profile.is_manager:
        qs = qs.filter(employee=profile)
    holiday_request = get_object_or_404(qs, pk=pk)
    #ensure admin employee cannot accept own request for holiday
    if holiday_request.employee != profile and holiday_request.status == 0:
        if request.POST:
            hol_auth_form = HolidayRequestAuthForm(request.POST, instance=holiday_request)
            if hol_auth_form.is_valid():
                holiday_request = hol_auth_form.save(commit=False)
                holiday_request.administrator = profile
                holiday_request.save()
                holiday_request.send_confirmation_email()
                return HttpResponseRedirect(reverse('holiday_user', kwargs={'username': profile.username}))
        else:
            hol_auth_form = HolidayRequestAuthForm(instance=holiday_request)
        context.update({'hol_auth_form': hol_auth_form})
    context.update({
        'holiday_request': holiday_request,
        'holidays': holiday_request.holiday_set,
    })
    return render_to_response('holiday/request_details.html', context)


@class_view_decorator(user_passes_test(is_manager))
class AllPendingRequestsList(ListView):
    model = HolidayRequest
    template_name = 'holiday/pending_requests.html'

    def get_queryset(self):
        qs = super(AllPendingRequestsList, self).get_queryset()
        return qs.filter(status=HolidayRequest.PENDING_STATUS)


class PendingRequestsList(AllPendingRequestsList):
    def get_queryset(self):
        qs = super(PendingRequestsList, self).get_queryset()
        return qs.filter(employee__manager__pk=self.request.user.pk)


@class_view_decorator(user_passes_test(is_manager))
class EmployeeList(ListView):
    model = Profile
    template_name = 'holiday/employee_list.html'


@class_view_decorator(login_required)
class HolidayCalendar(TemplateView):
    template_name = 'holiday/calendar.html'
