#!/usr/bin/env python
# -*- coding: utf-8 -*--

from kartotek.models import Vare
from django.contrib import admin


class VareAdmin(admin.ModelAdmin):
    list_display = ['nummer', 'navn', 'kategori','active', ]
    list_display_links =  ['nummer', 'navn', 'kategori', ]
    list_editable = ['active', ]
    list_filter = ['active', ]
    fields =       ['nummer', 'navn', 'kategori', ]


admin.site.register(Vare, VareAdmin)
