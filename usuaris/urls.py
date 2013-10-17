# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url

from usuaris import views

urlpatterns = patterns('',
    url(r'^$', views.loging, name='loging'),
    url(r'^accedir/$', views.accedir, name='accedir'),
    url(r'^llistat/$', views.llistat_usuaris, name='llistat'),
    url(r'^(?P<usuari_id>\d+)/$', views.detall_usuari, name='detall_usuari'),
)