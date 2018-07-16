# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from entities.api import EntityViewSet
from website.api import ConfigurationViewSet

admin.site.site_header = "Sakebowl"


router = routers.DefaultRouter()
router.register(r"entities", EntityViewSet, base_name="entities")
router.register(r"sites", ConfigurationViewSet, base_name="sites")


urlpatterns = [
    url(r"^api/", include(router.urls)),
    url(r"^auth/", views.obtain_auth_token),
    path('', admin.site.urls),
]
