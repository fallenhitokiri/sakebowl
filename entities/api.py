# -*- coding: utf-8 -*-
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view

from .models import Entity
from website.models import Configuration


class EntitySerializer(serializers.ModelSerializer):
    configuration_id = serializers.PrimaryKeyRelatedField(
        queryset=Configuration.objects.all(),
        source="configuration",
        write_only=True
    )

    class Meta:
        model = Entity
        fields = ("id", "title", "created_at", "updated_at", "published_at", "content", "configuration_id")


class EntityViewSet(viewsets.ModelViewSet):
    serializer_class = EntitySerializer

    def get_queryset(self):
        cid = self.request.GET["configuration"]
        return Entity.objects.filter(configuration_id=cid)
