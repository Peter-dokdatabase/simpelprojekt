#!/usr/bin/env python
# -*- coding: utf-8 -*--

from profil.models import Personale
from profil.models import Kreditor
from profil.models import Debitor
from django.contrib import admin

class PersonaleAdmin(admin.ModelAdmin):
    list_display = ['navn','active']
    list_editable = ['active']
    list_filter = ['active']
    fields = ['navn']

class KreditorAdmin(admin.ModelAdmin):
    list_display = ['navn','active']
    list_editable = ['active']
    list_filter = ['active']
    fields = ['navn','cvr','adresse','postnummer','by','email','telefonnummer']

class DebitorAdmin(admin.ModelAdmin):
    list_display = ['navn','active']
    list_editable = ['active']
    list_filter = ['active']
    fields = ['navn','cvr','adresse','postnummer','by','email','telefonnummer']

admin.site.register(Personale, PersonaleAdmin)
admin.site.register(Kreditor, KreditorAdmin)
admin.site.register(Debitor, DebitorAdmin)
