# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from .models import Addition
# Create your views here.


def index(request):
    obj=Addition.objects.get(id=1)
    obj.sum=obj.number1 + obj.number2
    obj.save()
    return render(request,'restapi/index.html',{'sum':obj.sum})