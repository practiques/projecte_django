# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url

from usuaris import views

urlpatterns = patterns('',
    url(r'^$', views.loging, name='loging'),
    url(r'^accedir/$', views.accedir, name='accedir'),
    url(r'^llistat/$', views.IndexView.as_view(), name='llistat'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detall_usuari'),
)