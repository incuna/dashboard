from django.template import Library

from imc.models import UserRating

register = Library()

@register.filter
def has_voted_for(user, movie):
    has_voted = True
    try:
        has_voted = UserRating.objects.get(user=user, movie=movie)
    except UserRating.DoesNotExist:
        has_voted = False
    return has_voted

