#!/usr/bin/env python
# -*- coding: utf-8 -*--

from django.db import models
from profil.models import Kreditor
from profil.models import Debitor
from profil.models import Personale
from kartotek.models import Vare

# Create your models here.

class Arbejdsseddel(models.Model):
    revideret = models.BooleanField(default=False)
    kreditor = models.ForeignKey(Kreditor)
    debitor = models.ForeignKey(Debitor)
    dato = models.DateField(auto_now_add=True)
    cpr = models.CharField(max_length=10)
    navn = models.CharField(max_length=100, blank=True)
    reference = models.ForeignKey(Personale)
    kommentar = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return str(self.id)
    #making a button for generating a Erkælæring in PDF
    def erklaering(self):
        return '<input type="button" value="PDF" onclick="location.href=\'pdf/%s/\'" />' % (self.pk)
    erklaering.short_description = 'Erklæring'
    erklaering.allow_tags = True

class ArbejdsseddelProdukter(models.Model):
    arbejdsseddel = models.ForeignKey(Arbejdsseddel)
    nummer = models.ForeignKey(Vare)
    beskrivelse = models.CharField(max_length=100, blank=True)



