#!/usr/bin/env python
# -*- coding: utf-8 -*--

from django.db import models

# Create your models here.

class Vare(models.Model):
    active = models.BooleanField(default=True)
    kategori_choices = (
        ('A', 'Aftagelig protetik'),
        ('B', 'Fast Protetik'),
        ('C', 'Implantatbehandling'),
        ('X', 'Diverse'),
    )
    navn =          models.CharField(max_length=100 )
    nummer =        models.CharField(max_length=4, primary_key=True)
    kategori =      models.CharField(max_length=1, choices=kategori_choices)
    def __unicode__(self):
        return str(self.nummer) + " " +  self.navn

