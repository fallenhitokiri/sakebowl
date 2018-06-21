# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Template


class ConfigurationFilter(admin.SimpleListFilter):
    title = "Site"
    parameter_name = "configuration"

    def lookups(self, request, model_admin):
        cfgs = set([e.configuration for e in model_admin.model.objects.all()])
        return [(c.id, c.name) for c in cfgs]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(configuration__id__exact=self.value())
        return queryset


class TemplateAdmin(admin.ModelAdmin):
    ordering = ("configuration__id", )
    list_filter = (ConfigurationFilter, )


admin.site.register(Template, TemplateAdmin)
