# -*- coding: utf-8 -*-
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view
from django_q.tasks import async_task
from rest_framework.response import Response

from .models import Configuration
from .tasks import deploy


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ("id", "name")


class ConfigurationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer


@api_view(['POST'])
def trigger_deploy(request, pk: int):
    async_task(deploy, pk)
    return Response({"status": "ok"})  # TODO: job ID for task fetch
