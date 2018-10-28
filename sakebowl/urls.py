"""sakebowl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from rest_framework import routers

from website.api import ConfigurationViewSet, trigger_deploy
from entities.api import EntityViewSet


admin.site.site_header = "Sakebowl"


router = routers.SimpleRouter()
router.register(r"websites", ConfigurationViewSet)
router.register(r"entities", EntityViewSet, base_name="entities")


urlpatterns = [
    path('', admin.site.urls),
    path(r"api/", include(router.urls)),
    path(r"api/websites/deploy/<int:pk>", trigger_deploy)
]

urlpatterns += staticfiles_urlpatterns()
