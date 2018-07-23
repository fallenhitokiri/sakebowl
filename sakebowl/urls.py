# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path

from entities import views as entities_views


admin.site.site_header = "Sakebowl"


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', entities_views.list_entities),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
