# -*- encoding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from usuaris.models import Usuari, Contrasenya
from django.views import generic
from django.utils import timezone



"""
Així quedaven la vista d'index i la vista de detall abans de fer servir vistes genèriques.

def llistat_usuaris(request):
	ultims_usuaris=Usuari.objects.order_by('-data_alta')[:5]
	return render_to_response('usuaris/llistat.html',{'ultims_usuaris': ultims_usuaris})

"""


class IndexView(generic.ListView):
	template_name='usuaris/llistat.html'
	context_object_name='ultims_usuaris'
	def get_queryset(self):
		return Usuari.objects.filter(data_alta__lte=timezone.now()).order_by('-data_alta')[:5]

class DetailView(generic.DetailView):
	model=Usuari
	template_name='usuaris/detall.html'

def detall_usuari(request,usuari_id):
	try:
		usuari=Usuari.objects.get(pk=usuari_id)
		data_alta_usu=usuari.data_alta
		if data_alta_usu<=timezone.now():
			return render_to_response('usuaris/detall.html',{'usuari': usuari})
		else:
			return HttpResponse("No s'ha trobat l'usuari")
	except (KeyError, Usuari.DoesNotExist):
		return HttpResponse("No s'ha trobat l'usuari")
	

def loging(request):
	return render(request,'usuaris/login.html')

def accedir(request):
	email_acces=request.POST['usu_acces']
	contra_acces=request.POST['contra_acces']
	try:
		usuari=Usuari.objects.get(correu=email_acces)
		contra_salt=usuari.contra_salt
		contra_hash=usuari.contra_hash
		if Contrasenya.generar_hash(contra_acces,contra_salt)==contra_hash:
			return render_to_response('usuaris/detall.html',{
				'usuari': usuari,
				'titol': u"Benvigut " + usuari.nom + u". Aquestes són les teves dades:"
				})
		else:
			ultims_usuaris=Usuari.objects.order_by('-data_alta')[:5]
			return render(request,'usuaris/usu_incorrecte.html')
	except (KeyError,Usuari.DoesNotExist):
		return render(request,'usuaris/usu_incorrecte.html')

		
	
