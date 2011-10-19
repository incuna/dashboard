from django.core.management.base import NoArgsCommand
from django.db.models import Max
import datetime

class Command(NoArgsCommand):
    help = 'Sync the holiday requests with Google calendar'

    def handle_noargs(self, **options):
        from holiday.models import HolidayRequest, holiday_request_observer
        
        for instance in HolidayRequest.objects.annotate(end_date=Max('holiday__date')).filter(end_date__gte=datetime.datetime.today):
            holiday_request_observer.update(HolidayRequest, instance)
