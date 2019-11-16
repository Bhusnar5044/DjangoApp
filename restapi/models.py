# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Addition(models.Model):
    number1=models.IntegerField(default=0)
    number2=models.IntegerField(default=0)
    sum=models.IntegerField(default=0)
