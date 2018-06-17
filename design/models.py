# -*- coding: utf-8 -*-
from django.db import models


class Template(models.Model):
    name = models.CharField(max_length=200)
    template = models.TextField()

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
