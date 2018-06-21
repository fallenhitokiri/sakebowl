# -*- coding: utf-8 -*-
from django.db import models

from drupan.entity import Entity as DrupanEntity

from website.models import Configuration


class Entity(models.Model):
    title = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    content = models.TextField()
    configuration = models.ForeignKey(
        Configuration,
        on_delete=models.DO_NOTHING,
        related_name="entities"
    )

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    @classmethod
    def as_list(cls, config):
        entities = list()
        for ent in cls.objects.exclude(published_at__isnull=True):
            meta = {
                "title": ent.title,
                "layout": "post",
                "date": ent.published_at
            }
            entity = DrupanEntity(config)
            entity.meta = meta
            entity.raw = ent.content.strip()
            entities.append(entity)
        return entities
