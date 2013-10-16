# -*- encoding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from usuaris.models import Usuari


# def llistat_usuaris(request):
# 	ultims_usuaris=Usuari.objects.order_by('-data_alta')[:5]
# 	output=', '.join([u.cognoms+", "+u.nom for u in ultims_usuaris])
# 	return HttpResponse(output)


def llistat_usuaris(request):
	ultims_usuaris=Usuari.objects.order_by('-data_alta')[:5]
	return render_to_response('usuaris/llistat.html',{'ultims_usuaris': ultims_usuaris})

def detall_usuari(request,usuari_id):
	usuari=get_object_or_404(Usuari,pk=usuari_id)
	#usuari=Usuari.objects.get(pk=usuari_id)
	return render_to_response('usuaris/detall.html',{'usuari': usuari})

def loging(request):
	return render(request,'usuaris/loging.html')

def accedir(request):
	usu_acces=request.POST['usu_acces']
	try:
		
		usuari=
	
		
	ultims_usuaris=Usuari.objects.order_by('-data_alta')[:5]
	return render_to_response('usuaris/llistat.html',{
				'ultims_usuaris': ultims_usuaris,
				'error_message': error_message
			})
