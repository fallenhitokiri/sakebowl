# -*- coding: utf-8 -*-
from django.db import models

from drupan.config import Config


class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    output = models.TextField()
    success = models.BooleanField()


class Configuration(models.Model):
    yaml = models.TextField()

    @classmethod
    def as_config(cls):
        cfg = Config()
        cfg.parse_yaml(cls.objects.first().yaml)
        return cfg
