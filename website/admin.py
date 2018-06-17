# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Log, Configuration


admin.site.register(Log)
admin.site.register(Configuration)
