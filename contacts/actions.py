from django.http import HttpResponse

from vobject import vCard
from vobject.vcard import Name

def build_card(contact):
    card = vCard()
    name = card.add('n')
    name.value = Name(family=contact.name)

    fullname = card.add('fn')
    if contact.user:
        fullname.value = '%s %s' % (contact.user.first_name, contact.user.last_name)
    else:
        fullname.value = contact.name

    tel = card.add('tel')
    tel.value = contact.extension
    return card.serialize()

def export(modeladmin, request, queryset):
    card = []
    for obj in queryset:
        card.append(build_card(obj))
    response = HttpResponse('\n'.join(card), mimetype='text/x-vcard')
    response['Content-Disposition'] = 'attachment; filename=incuna.vcf'
    return response

