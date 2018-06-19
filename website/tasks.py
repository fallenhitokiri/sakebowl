# -*- coding: utf-8 -*-
from .models import Configuration
from entities.models import Entity
from design.models import Template

from drupan.engine import Engine


def deploy():
    config = Configuration.as_config()
    templates = Template.as_dict()
    entities = Entity.as_list(config)

    engine = Engine()
    engine.site.templates = templates
    engine.site.entities = entities
    engine.config = config

    engine.prepare_engine()
    engine.run()
