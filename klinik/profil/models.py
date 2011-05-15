#!/usr/bin/env python
# -*- coding: utf-8 -*--

from django.db import models

# Create your models here.

class Personale(models.Model):
    active = models.BooleanField(default=True)
    navn = models.CharField(max_length=200, primary_key=True)
    def __unicode__(self):
        return self.pk


class Kreditor(models.Model):
    active = models.BooleanField(default=True)
    navn = models.CharField(max_length=200, primary_key=True)
    adresse = models.CharField(max_length= 200)
    postnummer = models.CharField(max_length= 20, blank=True)
    by = models.CharField(max_length= 20, blank=True)
    telefonnummer = models.CharField(max_length=20,default='+45 ', blank=True)
    cvr = models.CharField(max_length=8, default='00000000', blank=True)
    email = models.EmailField(max_length=75, blank=True)
    def __unicode__(self):
        return self.pk


class Debitor(models.Model):
    active = models.BooleanField(default=True)
    navn = models.CharField(max_length=200, primary_key=True)
    adresse = models.CharField(max_length=200)
    postnummer = models.CharField(max_length= 20, blank=True)
    by = models.CharField(max_length= 20, blank=True)
    telefonnummer = models.CharField(max_length=20,default='+45 ', blank=True)
    cvr = models.CharField(max_length=8, default='00000000', blank=True)
    email = models.EmailField(max_length=75, blank=True)
    def __unicode__(self):
        return self.pk

