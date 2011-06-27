from django.http import HttpResponse
from mechanize import Browser
from vobject import vCard
from vobject.vcard import Name

def _build_directory(queryset):
    directory = []
    for contact in queryset:
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
        directory.append(card.serialize())
    return '\n'.join(directory)

def export(modeladmin, request, queryset):
    response = HttpResponse(_build_directory(queryset), mimetype='text/x-vcard')
    response['Content-Disposition'] = 'attachment; filename=incuna.vcf'
    return response

def update_handsets(modeladmin, request, queryset):
    directory = _build_directory(queryset)
    # make directory seem like a real file!

    # user mechanize to push this to every handset
    br = Browser()
    br.open("http://192.168.0.3/login.html")
    br.select_form(name="gigaset")
    br['password'] = '0000'
    br.submit()

    # get a list of handsets?
    for i in range(0, 4):
        # submit to http://192.168.0.3/settings_telephony_tdt.html, need to get past the login
        pass

