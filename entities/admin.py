# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Entity


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


class PublishedFilter(admin.SimpleListFilter):
    title = "Published"
    parameter_name = "published_at"
    choice_published = "Published"
    choice_draft = "Draft"

    def lookups(self, request, model_admin):
        return [
            (self.choice_published, self.choice_published),
            (self.choice_draft, self.choice_draft)
        ]

    def queryset(self, request, queryset):
        if self.value():
            if self.value() == self.choice_published:
                return queryset.filter(published_at__isnull=False)
            else:
                return queryset.filter(published_at__isnull=True)
        return queryset


class EntityAdmin(admin.ModelAdmin):
    fields = (("title", "published_at", "configuration"), "content")
    list_display = ("title", "published_at", "updated_at")
    # TODO: admin.SimpleListFilter for publishedAt (Draft status)
    ordering = ("-published_at",)
    search_fields = ("title", "content")
    list_filter = (ConfigurationFilter, PublishedFilter)


admin.site.register(Entity, EntityAdmin)
