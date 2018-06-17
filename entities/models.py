# -*- coding: utf-8 -*-
from django.db import models

from drupan.entity import Entity as DrupanEntity

class Entity(models.Model):
    title = models.CharField(max_length=2000)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    publishedAt = models.DateTimeField(blank=True, null=True)
    content = models.TextField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    @classmethod
    def as_list(cls, config):
        entities = list()
        for ent in cls.objects.exclude(publishedAt__isnull=True):
            meta = {
                "title": ent.title,
                "layout": "post",
                "date": ent.publishedAt
            }
            entity = DrupanEntity(config)
            entity.meta = meta
            entity.raw = ent.content.strip()
            entities.append(entity)
        return entities
