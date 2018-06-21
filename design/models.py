# -*- coding: utf-8 -*-
from django.db import models

from website.models import Configuration


class Template(models.Model):
    name = models.CharField(max_length=200)
    template = models.TextField()
    configuration = models.ForeignKey(
        Configuration,
        on_delete=models.DO_NOTHING,
        related_name="templates"
    )

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    @classmethod
    def as_dict(cls):
        templates = dict()
        for temp in cls.objects.all():
            templates[temp.name] = temp.template
        return templates
