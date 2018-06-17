# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Entity


class EntityAdmin(admin.ModelAdmin):
    fields = (("title", "publishedAt"), "content")
    list_display = ("title", "publishedAt", "updatedAt")
    # TODO: admin.SimpleListFilter for publishedAt (Draft status)
    ordering = ("-publishedAt",)
    search_fields = ("title", "content")


admin.site.register(Entity, EntityAdmin)
