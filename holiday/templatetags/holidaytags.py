from django import template
from django.template import Library
from holiday.models import HolidayRequest

register = Library()

@register.filter
def days_left_by_year(employee, year_offset=0):
    return employee.days_left_count(year_offset)

@register.filter
def days_requested_by_year(holiday_request, year_offset=0):
    return holiday_request.days_requested_count(year_offset)

class AllPendingRequests(template.Node):
    """
    Returns all pending requests into the named context.
    """
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        items = HolidayRequest.objects.filter(status__exact=0)

        context[self.var_name] = items
        return ''


def do_all_pending_requests(parser, token):
    """
    Gets a list of items related via a tag.

    Syntax:
        {% all_pending_requests as [varname] %}

    Example::
        {% all_pending_requests as all_of_em %} (gets the pending requests)

    """
    bits = token.contents.split()
    if len(bits) != 3:
        raise template.TemplateSyntaxError("'%s' tag takes three arguments" % bits[0])
    if bits[1] != 'as':
        raise template.TemplateSyntaxError("first argument to '%s' tag must be 'as'" % bits[0])
    return AllPendingRequests(bits[2])


register.tag('all_pending_requests', do_all_pending_requests)