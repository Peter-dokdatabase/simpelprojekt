#!/usr/bin/env python
# -*- coding: utf-8 -*--

# Create your views here.

from django.contrib.auth.models import User
from django.http import HttpResponse

def printTest(request):
    u = User.objects.get(pk=2)
    ls = u.get_all_permissions(obj=None)
    s = ""
    for p in ls:
        s = s + str(p) + ", "
    return HttpResponse(s)

