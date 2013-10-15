# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url

from usuaris import views

urlpatterns = patterns('',
    url(r'^$', views.llistat_usuaris, name='llistat_usuaris'),
    url(r'^(?P<usuari_id>\d+)/$', views.detall_usuari, name='detall_usuari'),
)