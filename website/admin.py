# -*- coding: utf-8 -*-
from django.contrib import admin

from django_q.tasks import async

from .models import Log, Configuration
from .tasks import deploy


def publish(modeladmin, request, queryset):
    async(deploy)


publish.short_description = "publish website"


class ConfigurationAdmin(admin.ModelAdmin):
    actions = (publish, )

    def changelist_view(self, request, extra_context=None):
        """Select first configuration item for publish to allow running the
        command without requiring a selection.

        This needs to be removed for a multi-site setup.
        """
        if "action" in request.POST and request.POST["action"] == "publish":
            post = request.POST.copy()
            cfg = Configuration.objects.first()
            post.update({admin.ACTION_CHECKBOX_NAME: str(cfg.id)})
            request._set_post(post)
        return super().changelist_view(request, extra_context)


admin.site.register(Log)
admin.site.register(Configuration, ConfigurationAdmin)
