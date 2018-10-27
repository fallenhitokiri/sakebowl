# -*- coding: utf-8 -*-
from rest_framework import serializers, viewsets

from .models import Configuration


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ("id", "name")


class ConfigurationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer
