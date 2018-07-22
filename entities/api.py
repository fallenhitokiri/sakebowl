# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework import viewsets

from .models import Entity


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ("id", "title", "created_at", "updated_at", "published_at", "content", "configuration")


class EntityViewSet(viewsets.ModelViewSet):
    serializer_class = EntitySerializer

    def get_queryset(self):
        name = self.request.query_params["name"]
        return Entity.objects.filter(configuration__name=name)
