# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Addition

# Register your models here.
class AdditionAdmin(admin.ModelAdmin):
    list_display=('number1','number2','sum')

admin.site.register(Addition, AdditionAdmin)