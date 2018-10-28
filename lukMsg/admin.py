# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import LukInfo, LukUser

# Register your models here.


admin.site.register(LukInfo)
admin.site.register(LukUser)