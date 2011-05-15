#!/usr/bin/env python
# -*- coding: utf-8 -*--

from dokument.models import Arbejdsseddel
from dokument.models import ArbejdsseddelProdukter
from django.contrib import admin
from profil.models import  Kreditor, Debitor, Personale


#ekstra class for adding 'attributter' when inserting a 'vare'
class ArbejdsseddelProdukterInline(admin.TabularInline):
    model = ArbejdsseddelProdukter
    extra = 3


class ArbejdsseddelAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "kreditor":
            kwargs["queryset"] = Kreditor.objects.filter(active=True)
        if db_field.name == "debitor":
            kwargs["queryset"] = Debitor.objects.filter(active=True)
        if db_field.name == "reference":
            kwargs["queryset"] = Personale.objects.filter(active=True)
        return super(ArbejdsseddelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    fieldsets = (
                (None, {'fields':
                        (('kreditor','debitor'),
                         'reference',
                         ('cpr','navn'),
                         'kommentar',
    ) } ), )
    radio_fields = {"reference": admin.VERTICAL}

    #what to display in list
    list_display = ['id', 'debitor', 'dato', 'cpr', 'reference',
                    'revideret','erklaering']
    list_display_links = ['id', 'debitor', 'dato', 'cpr', 'reference']

    list_editable = ['revideret']
    list_filter = ['dato', 'revideret']
    date_hierarchy = 'dato'
    search_fields = ['^cpr']

    #put an ekstra save button on the top
    save_on_top = True

    #enable posibilities to add Produkter to Arbejdsseddel
    inlines =[ArbejdsseddelProdukterInline]


class ArbejdsseddelProdukterAdmin(admin.ModelAdmin):
    list_display = ['arbejdsseddel', 'nummer', 'beskrivelse']
    fields = ['arbejdsseddel', 'nummer', 'beskrivelse']



admin.site.register(Arbejdsseddel, ArbejdsseddelAdmin)
# admin.site.register(ArbejdsseddelProdukter, ArbejdsseddelProdukterAdmin)

