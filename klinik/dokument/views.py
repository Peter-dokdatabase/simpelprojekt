# Create your views here.
# -*- encoding: utf-8 -*-#

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
from django.template.defaultfilters import slugify
from django.shortcuts import get_object_or_404
from dokument.models import Arbejdsseddel, ArbejdsseddelProdukter
from kartotek.models import Vare

def printPDF(request, arbj_id):
	# Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    a = get_object_or_404(Arbejdsseddel, pk=arbj_id)
    response['Content-Disposition'] = 'attachment; filename=' +  str(a.id) + '.pdf'
    # Laver toppen med hvem dokumentet er til
    p.setTitle(str(a.id))
    p.setFont("Helvetica", 8)
    p.drawString(80, 755, "Udstyret er udført på grundlag af ordre/recept fra:")
    p.setFontSize(12)
    p.drawString(80,730, a.debitor.navn)
    p.drawString(80,710, a.debitor.adresse)
    p.setFontSize(8)
    p.drawString(80,670, "Medfølgende medicinske udstyr efter mål, tandprotetisk")
    p.drawString(80,650, "arbejde, er til brug for nedenstående patient:")
    p.setFontSize(12)
    p.drawString(80,630, a.cpr)
    p.drawString(80,610, a.navn)
    #
    p.setFontSize(9)
    p.drawString(80,570, "Obligatorisk, Klasse lla, fast protetik:")

    produktBox = p.beginText(100, 5)
    produktBox.setTextOrigin(80, 550)
    produktBox.setFont("Helvetica-Oblique", 10)
    for v in ArbejdsseddelProdukter.objects.filter(arbejdsseddel=arbj_id):
        if (v.nummer.kategori == 'B') | (v.nummer.kategori == 'C'):
            produktBox.textLine(v.nummer.navn + ":  " + v.beskrivelse)
    p.drawText(produktBox)

    p.setFontSize(9)
    p.drawString(80,350, "Frivilligt klasse l, aftagelig protetik:")
    frivilligBox = p.beginText(100,5)
    frivilligBox.setTextOrigin(80,330)
    frivilligBox.setFont("Helvetica-Oblique", 10)
    for v in ArbejdsseddelProdukter.objects.filter(arbejdsseddel=arbj_id):
        if (v.nummer.kategori == 'A') | (v.nummer.kategori == 'X'):
            frivilligBox.textLine(v.nummer.navn + ": " + v.beskrivelse)
    p.drawText(frivilligBox)

    p.setFontSize(9)
    p.drawString(80,180, "Kommentar:")
    p.drawString(80,160, a.kommentar)
    # Laver delen af bundet med lovkravet
    p.setFontSize(8)
    p.drawString(50,90,"Det bekræftes herved, at ovennævnte medicinske udstyr efter mål er fremstillet i overensstemmelse med Sundhedsministeriet bekentgørelse")
    p.drawString(50,80,"nr 734 af 10. august 1994, og EU direktiv 43/92 af 14. juni 1993, om medicinsk udstyr, herunder at det opfylder de væsenlige krav i")
    p.drawString(50,70,"bekendtgørelsen jvf. bilag 1. Såfremt der er undtagelser i disse væsenlige krav, er disse undtagelser nævnt ovenfor.")
    # Laver bundet med Danske Dental Laboratorier
    p.drawImage('/home/ptk/simpelprojekt/klinik/dokument/DDL.jpg',30,40,width=30,height=30)
    p.setFontSize(6)
    p.drawString(32,38, "Medlem af")
    p.drawString(32,33, "Danske Dental Laboratorier")
    p.line(110,33,460,33)
    p.line(35,70,35,500)
    p.setFontSize(9)
    p.drawString(465,33, "Vi lever op til kravene")
    p.drawString(145,47, "Fabrikantens underskrift:_________________________________________")
    # Laver reipurth dental information i øvre højre hjørne
    p.setFontSize(12)
    p.line(370,770,570,770)
    p.setFont("Helvetica-Bold", 12)
    p.drawString(370,750, "Reipurth Dental")
    p.setFont("Helvetica", 80)
    p.setFontSize(9)
    p.drawString(370,730, a.kreditor.navn)
    p.drawString(370,710, "2605 Brøndby")
    p.drawString(370,690, "Tlf: " + str(a.kreditor.telefonnummer))
    p.drawString(370,670, "cvr: " + str(a.kreditor.cvr))
    # Laver delen med erklæring til tandlæge
    p.line(370,615,570,615)
    p.setFont("Helvetica-Bold", 12)
    p.drawString(370,600, "ERKLÆRING TIL PATIENT")
    p.setFont("Helvetica", 80)
    p.setFontSize(9)
    p.drawString(370,580, "VEDRØRENDE MEDICINSK UDSTYR EFTER MÅL")
    p.setFontSize(7)
    p.drawString(370,560, "Ved eventuel henvendelse opgiv nedenstående nummer:")
    p.setFontSize(9)
    p.drawString(370,540, "Ordre/recept nr.: " + str(a.id))
    p.drawString(370,520, "Dato: " + str(a.dato))
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
  #  boldtest = p.getAvailableFonts()
  #  response = HttpResponse(boldtest)
    return response
"""
from django.db import models
from django import forms
from django.forms import ModelForm
from django.forms.widgets import RadioSelect
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from profil.models import Kreditor, Debitor, Personale
from dokument.models import Arbejdsseddel
"""
