# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^usuaris/', include('usuaris.urls',namespace='usuaris')),
    url(r'^admin/', include(admin.site.urls)),
)
