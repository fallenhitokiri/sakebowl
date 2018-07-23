# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, get_list_or_404, render

from entities.models import Entity
from website.models import Configuration


def list_entities(request, website=None):
    websites = Configuration.objects.all()

    if website:
        active = websites.get(id=id)
    else:
        active = websites.first()

    entities = Entity.objects.filter(configuration__id=active.id).order_by("published_at")

    ctx = {
        "websites": websites,
        "entities": entities
    }

    return render(request, "entities/list.html", ctx)
