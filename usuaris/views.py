# -*- encoding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from usuaris.models import Usuari


# def llistat_usuaris(request):
# 	ultims_usuaris=Usuari.objects.order_by('-data_alta')[:5]
# 	output=', '.join([u.cognoms+", "+u.nom for u in ultims_usuaris])
# 	return HttpResponse(output)


def llistat_usuaris(request):
	ultims_usuaris=Usuari.objects.order_by('-data_alta')[:5]
	context={'ultims_usuaris': ultims_usuaris}
	return render(request,'usuaris/llistat.html',context)

def detall_usuari(request,usuari_id):
	usuari=Usuari.objects.get(pk=usuari_id)
	context={'usuari': usuari}
	return render(request,'usuaris/detall.html',context)

def loging(request):
	return render(request,'usuaris/loging.html')

def accedir(request):
	return render(request,'usuaris/llistat_usuaris.html')