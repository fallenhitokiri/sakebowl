# -*- coding: utf-8 -*-
from rest_framework import serializers, viewsets

from .models import Configuration


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ("name", )


class ConfigurationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ConfigurationSerializer
    queryset = Configuration.objects.all()
