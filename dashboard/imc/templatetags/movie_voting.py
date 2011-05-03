from django.template import Library

from imc.models import EmployeeRating

register = Library()

@register.filter
def has_voted_for(employee, movie):
    has_voted = True
    try:
        has_voted = EmployeeRating.objects.get(employee=employee, movie=movie)
    except EmployeeRating.DoesNotExist:
        has_voted = False
    return has_voted

