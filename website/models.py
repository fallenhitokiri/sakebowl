# -*- coding: utf-8 -*-
from django.db import models

from drupan.config import Config


class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    output = models.TextField()
    success = models.BooleanField()


class Configuration(models.Model):
    name = models.CharField(max_length=200)
    yaml = models.TextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def as_config(self):
        cfg = Config()
        cfg.parse_yaml(self.yaml)
        return cfg
