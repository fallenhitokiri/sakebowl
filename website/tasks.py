# -*- coding: utf-8 -*-
from django_q.tasks import async

from .models import Log


def deploy():
    async(__deploy)


def __deploy():
    Log.objects.create(success=True, output="foobar")
