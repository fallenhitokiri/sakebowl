# -*- coding: utf-8 -*-
from django.contrib import admin

from django_q.tasks import async_task

from .models import Log, Configuration
from .tasks import deploy


def publish(modeladmin, request, queryset):
    for cfg in queryset.all():
        async_task(deploy, cfg.id)


publish.short_description = "publish website"


class ConfigurationAdmin(admin.ModelAdmin):
    actions = (publish, )


admin.site.register(Log)
admin.site.register(Configuration, ConfigurationAdmin)
