import json

from django.http import HttpResponse
from django.views.generic.list import BaseListView

from models import Item


class Json(BaseListView):
    queryset = Item.objects.filter(bought=False).order_by('created')

    def get_json_data(self):
        json_context = []
        if self.object_list.count() > 9:
            json_context.append({'more': self.object_list.count() - 8})
            self.object_list = self.object_list[:8]
        [json_context.append({'name': item.name}) for item in self.object_list]
        return json_context

    def render_to_response(self, context):
        return HttpResponse(json.dumps(self.get_json_data()), mimetype='application/json')

