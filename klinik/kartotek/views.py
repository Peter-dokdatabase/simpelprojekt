#!/usr/bin/env python
# -*- coding: utf-8 -*--

from django.utils.html import escape

# Create your views here.
from django.http import HttpResponse


def filldata(request):
    #create users
    from django.contrib.auth.models import User

    #creating a normal staff user
    user = User.objects.create_user('reiphurt', 'base@gmail.com',
                                    'hvidtand')
    user.is_staff = True
    user.is_superuser = False
    """ TODO
    # adding permissions except deleting operations
    user.user_permissions = [profil.add_personale,
                             kartotek.change_vare,
                             profil.add_debitor,
                             profil.change_debitor,
                             profil.add_kreditor,
                             dokument.add_arbejdsseddel,
                             kartotek.add_vare,
                             dokument.change_arbejdsseddel,
                             dokument.add_arbejdsseddelprodukter,
                             dokument.change_arbejdsseddelprodukter,
                             profil.change_kreditor,
                             profil.change_personale,
                            ]
    """
    user.save()
    #creating a superuser
    user = User.objects.create_user('ptk', 'dokdatabase@gmail.com', 'a')
    user.is_staff = True
    user.is_superuser = True
    user.save()

    #Inserting into kreditor
    from profil.models import Kreditor
    p = Kreditor(navn="Reipurth Dental",
                 adresse="Nygaards Plads 3d 1 th, 2605 Brøndby",
                 telefonnummer='+45 26 27 07 31',
                 cvr='12345678',
                 email="jakob@reipurth-dental.dk",
                )
    p.save()

    #Inserting into debitor
    from profil.models import Debitor
    p = Debitor(navn="klaus laege",
                adresse='Jagtvej 12',
                telefonnummer='+45 23456789',
                cvr='23456789')
    p.save()

    p = Debitor(navn="Tandlaegehuset",
                adresse='Tandvej 45',
                telefonnummer='+45 23462454',
                cvr='98765432')
    p.save()

    p = Debitor(navn="Sweeney Todd",
                adresse='Fleetstreet',
                telefonnummer='+45 666',
                cvr='97864523')
    p.save()

    p = Debitor(navn="The Dentist",
                adresse='Elmstreet 66',
                telefonnummer='+45 31224455',
                cvr='24375698')
    p.save()

    p = Debitor(navn="Doktor Banner",
                adresse='Hulkgade 44',
                telefonnummer='+45 77889900',
                cvr='12345678')
    p.save()

    #inserting into personale.
    from profil.models import Personale

    for pers in ['Pernille','Trine','Jacob','Cristoffer']:
        p = Personale(navn = pers)
        p.save()


    #inserting values in Vare
    from kartotek.models import Vare

    p = Vare(navn="Model",
             nummer="100",
             kategori='X')
    p.save()

    p = Vare(navn="Modelarbejde",
             nummer="101",
             kategori='X')
    p.save()

    p = Vare(navn="Aftrykske",
             nummer="102",
             kategori='A')
    p.save()

    p = Vare(navn="Plastron",
             nummer="103",
             kategori='A')
    p.save()

    p = Vare(navn="Opstilling HO/UH",
             nummer="104",
             kategori='A')
    p.save()

    p = Vare(navn="Opstilling helsæt",
             nummer="105",
             kategori='A')
    p.save()

    p = Vare(navn="Montering HO/HU",
             nummer="106",
             kategori='A')
    p.save()

    p = Vare(navn="Duplikering HO/HU",
             nummer="107",
             kategori='A')
    p.save()

    p = Vare(navn="Rebasering HO/HU",
             nummer="108",
             kategori='A')
    p.save()

    p = Vare(navn="Opstilling 2-3 tænder",
             nummer="109",
             kategori='A')
    p.save()

    p = Vare(navn="Opstilling 4-8 tænder",
             nummer="110",
             kategori='A')
    p.save()

    p = Vare(navn="Opstilling 9-14 tænder",
             nummer="111",
             kategori='A')
    p.save()

    p = Vare(navn="Montering 2-3 tænder",
             nummer="112",
             kategori='A')
    p.save()

    p = Vare(navn="Montering 4-8 tænder",
             nummer="113",
             kategori='A')
    p.save()

    p = Vare(navn="Montering 9-14 tænder",
             nummer="114",
             kategori='A')
    p.save()

    p = Vare(navn="Blød bideskinne",
             nummer="115",
             kategori='X')
    p.save()

    p = Vare(navn="Påsætning af tand/bøjle",
             nummer="116",
             kategori='A')
    p.save()

    p = Vare(navn="Protese rep (simpel)",
             nummer="117",
             kategori='A')
    p.save()

    p = Vare(navn="Protese rep (kompliceret)",
             nummer="118",
             kategori='A')
    p.save()

    p = Vare(navn="Udvidelse tand/bøjle",
             nummer="119",
             kategori='A')
    p.save()

    p = Vare(navn="Enkel el. L bøjle",
             nummer="120",
             kategori='A')
    p.save()

    p = Vare(navn="Dobbelt el. T bøjle",
             nummer="121",
             kategori='A')
    p.save()

    p = Vare(navn="3 mm refleksfrigørende bideskinne",
             nummer="122",
             kategori='X')
    p.save()

    p = Vare(navn="Smile protese (1 tand)",
             nummer="123",
             kategori='A')
    p.save()

    p = Vare(navn="Durasoft",
             nummer="124",
             kategori='X')
    p.save()

    p = Vare(navn="Argenco 68 Guld",
             nummer="125",
             kategori='B')
    p.save()

    p = Vare(navn="Gingiva",
             nummer="126",
             kategori='X')
    p.save()

    p = Vare(navn="Styreskinne",
             nummer="127",
             kategori='C')
    p.save()

    p = Vare(navn="Opmodelleret ophæng",
             nummer="128",
             kategori='X')
    p.save()

    p = Vare(navn="Finer",
             nummer="200",
             kategori='B')
    p.save()

    p = Vare(navn="Dir. støbning",
             nummer="201",
             kategori='B')
    p.save()

    p = Vare(navn="Partiel krone",
             nummer="202",
             kategori='B')
    p.save()

    p = Vare(navn="MK krone",
             nummer="203",
             kategori='B')
    p.save()

    p = Vare(navn="Sammenlodning",
             nummer="204",
             kategori='B')
    p.save()

    p = Vare(navn="Støbt stel (unitor)",
             nummer="205",
             kategori='A')
    p.save()

    p = Vare(navn="Farveprøve",
             nummer="206",
             kategori='X')
    p.save()

    p = Vare(navn="Mk guld (Esteticor +)",
             nummer="207",
             kategori='B')
    p.save()

    p = Vare(navn="Mk. bro pr led",
             nummer="208",
             kategori='B')
    p.save()

    p = Vare(navn="Stampe",
             nummer="209",
             kategori='X')
    p.save()

    p = Vare(navn="Ekspeditionsgebyr",
             nummer="210",
             kategori='X')
    p.save()

    p = Vare(navn="Montering implantat (Fast protetik)",
             nummer="211",
             kategori='B')
    p.save()

    p = Vare(navn="Implantat mk Krone",
             nummer="226",
             kategori='C')
    p.save()

    p = Vare(navn="Atlantic Abutment",
             nummer="229",
             kategori='C')
    p.save()

    p = Vare(navn="Mk (tilbud)",
             nummer="230",
             kategori='B')
    p.save()

    p = Vare(navn="Finer (tilbud)",
             nummer="231",
             kategori='B')
    p.save()

    p = Vare(navn="Montering af attachment",
             nummer="232",
             kategori='B')
    p.save()

    p = Vare(navn="Støbt Opbygning",
             nummer="233",
             kategori='B')
    p.save()

    p = Vare(navn="Protese guldtand",
             nummer="234",
             kategori='B')
    p.save()

    p = Vare(navn="Nobel Biocare attachment",
             nummer="235",
             kategori='C')
    p.save()

    p = Vare(navn="Pallorag (opbygning)",
             nummer="236",
             kategori='B')
    p.save()

    p = Vare(navn="Blegeskinne",
             nummer="237",
             kategori='X')
    p.save()

    p = Vare(navn="Skulder procelæn",
             nummer="238",
             kategori='B')
    p.save()

    p = Vare(navn="efterfølgende tand (protese)",
             nummer="239",
             kategori='A')
    p.save()

    p = Vare(navn="Krone tilpasset unitor",
             nummer="240",
             kategori='B')
    p.save()

    p = Vare(navn="1x8 vita",
             nummer="241",
             kategori='A')
    p.save()

    p = Vare(navn="1x6 vita",
             nummer="242",
             kategori='A')
    p.save()

    p = Vare(navn="Protese tand",
             nummer="243",
             kategori='A')
    p.save()

    p = Vare(navn="Indmaling",
             nummer="244",
             kategori='B')
    p.save()

    p = Vare(navn="Ætsbro",
             nummer="245",
             kategori='B')
    p.save()

    p = Vare(navn="Ips e.max",
             nummer="246",
             kategori='B')
    p.save()

    p = Vare(navn="Afmontering af unitor",
             nummer="247",
             kategori='A')
    p.save()

    p = Vare(navn="Argelite (Mk Guld)",
             nummer="248",
             kategori='B')
    p.save()

    p = Vare(navn="Straumann SynOcta",
             nummer="250",
             kategori='C')
    p.save()

    p = Vare(navn="Straumann SynOcta Analog",
             nummer="251",
             kategori='C')
    p.save()

    p = Vare(navn="Implantat styreskinne",
             nummer="252",
             kategori='C')
    p.save()

    p = Vare(navn="parapost",
             nummer="253",
             kategori='B')
    p.save()

    p = Vare(navn="Implantat Replica (Nobel Replace)",
             nummer="254",
             kategori='C')
    p.save()

    p = Vare(navn="Locator (Male, Nobel)",
             nummer="255",
             kategori='C')
    p.save()

    p = Vare(navn="Locator (Female, Nobel)",
             nummer="256",
             kategori='C')
    p.save()

    p = Vare(navn="5,00mm Locator Abutment",
             nummer="257",
             kategori='C')
    p.save()

    p = Vare(navn="Porcelæn korrektur",
             nummer="258",
             kategori='B')
    p.save()

    p = Vare(navn="Vivodent fortænder",
             nummer="259",
             kategori='A')
    p.save()

    p = Vare(navn="Vivodent Kindtænder",
             nummer="260",
             kategori='A')
    p.save()

    p = Vare(navn="Unitor",
             nummer="261",
             kategori='A')
    p.save()

    p = Vare(navn="Öwall bøjle Au",
             nummer="262",
             kategori='A')
    p.save()

    p = Vare(navn="Retentionstråd",
             nummer="263",
             kategori='X')
    p.save()

    p = Vare(navn="Synocta opbygning (straumann)",
             nummer="264",
             kategori='C')
    p.save()

    p = Vare(navn="Straumann gipsanalog (RN)",
             nummer="265",
             kategori='X')
    p.save()

    p = Vare(navn="Ortho Studiemodeller",
             nummer="266",
             kategori='X')
    p.save()

    p = Vare(navn="Kørsel",
             nummer="300",
             kategori='X')
    p.save()






    #give a finish message
    return HttpResponse("database is filled with test data")
#"""
