# -*- coding: utf-8 -*-
from .models import Log, Configuration
from entities.models import Entity
from design.models import Template

from drupan.engine import Engine


def deploy(pk: int):
    """deploy loads the configuration for a given primary key and runs drupans
    engine with the configuration stored in sakebowl.
    """
    cfg_obj = Configuration.objects.get(pk=pk)
    config = cfg_obj.as_config()
    templates = Template.as_dict()
    entities = Entity.as_list(config)

    engine = Engine()
    engine.site.templates = templates
    engine.site.entities = entities
    engine.config = config

    engine.prepare_engine()
    engine.run()
