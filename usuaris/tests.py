# -*- encoding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import timezone
from usuaris.models import *
import datetime
from django.core.urlresolvers import reverse
from usuaris.views import *

class UsuarisMethodTests(TestCase):

	def test_usuari_creat_recentment_amb_data_futura(self):
		time = timezone.now() + datetime.timedelta(days=30)
		usuari_futur = Usuari(nom='Nom',cognoms='Cognom1 Cognom2',data_alta=time,correu='r@r.com',edat=1)
		self.assertEqual(usuari_futur.creat_recentment(), False)

	def test_usuari_creat_recentment_amb_data_darrer_dia(self):
		time = timezone.now() - datetime.timedelta(hours=12)
		usuari = Usuari(nom='Nom',cognoms='Cognom1 Cognom2',data_alta=time,correu='r@r.com',edat=1)
		self.assertEqual(usuari.creat_recentment(), True)

	def test_any_de_naixement_positiu(self):
		any_actual = timezone.now().year
		data_alta_usu = timezone.now() -datetime.timedelta(days=400)
		usuari = Usuari(nom="Nom",cognoms="Cognom1 Cognom2",data_alta=data_alta_usu,correu='usu@usu.com',edat=1)
		any_naix = any_actual - usuari.edat
		self.assertEqual(any_naix > 0, True)



class UsuariIndexViewTests(TestCase):
	"""
	Index és el llistat d'usuaris al qual l'usuari pot accedir una vegda s'hagi autenticat.
	"""
	
	def test_index_vista_retorna_ok(self): 	
		"""
		Retorna status 200 en accedir a la vista.
		"""
		response=self.client.get(reverse('usuaris:llistat'))
		self.assertEqual(response.status_code,200)		

	def test_index_sense_usuaris(self):
		"""
		Retorna missatge adient quan no s'han donat d'alta usuaris
		"""
		response=self.client.get(reverse('usuaris:llistat'))
		self.assertContains(response, 'No existeixen usuaris')
		self.assertQuerysetEqual(response.context['ultims_usuaris'], [])

	def test_index_amb_usuaris_passats(self):
		"""
		Retorna tots els usuaris que han estat donats d'alta
		"""
		data_alta_usu = timezone.now() - datetime.timedelta(days=300)
		carrec1=Carrec.objects.create(nom=u'Carrec 1', descr=u'Descripció càrrec 1')
		carrec2=Carrec.objects.create(nom=u'Carrec 2', descr=u'Descripció càrrec 2')
		Usuari.objects.create(nom="Nom1", cognoms="PrimerCogn1 SegonCogn1", data_alta=data_alta_usu, correu='usu1@usu.com', edat=45, carrec=carrec1)
		Usuari.objects.create(nom="Nom2", cognoms="PrimerCogn2 SegonCogn2", data_alta=data_alta_usu,correu='usu2@usu.com',edat=45, carrec=carrec2)
		usuaris=IndexView().get_queryset()
		response=self.client.get(reverse('usuaris:llistat'))
		self.assertQuerysetEqual(
			response.context['ultims_usuaris'],
			['<Usuari: PrimerCogn1 SegonCogn1, Nom1>', '<Usuari: PrimerCogn2 SegonCogn2, Nom2>']
		)

	def test_index_amb_usuari_futur(self):
		"""
		No retorna usuaris que s'han afegit a la bbdd però amb una data d'alta futura.
		"""
		data_alta_usu1 = timezone.now() - datetime.timedelta(days=300)
		data_alta_usu2 = timezone.now() + datetime.timedelta(days=300)
		carrec1=Carrec.objects.create(nom=u'Carrec 1', descr=u'Descripció càrrec 1')
		carrec2=Carrec.objects.create(nom=u'Carrec 2', descr=u'Descripció càrrec 2')
		Usuari.objects.create(nom="Nom1", cognoms="PrimerCogn1 SegonCogn1", data_alta=data_alta_usu1, correu='usu1@usu.com', edat=45, carrec=carrec1)
		Usuari.objects.create(nom="Nom2", cognoms="PrimerCogn2 SegonCogn2", data_alta=data_alta_usu2,correu='usu2@usu.com',edat=45, carrec=carrec2)
		usuaris=IndexView().get_queryset()
		response=self.client.get(reverse('usuaris:llistat'))
		self.assertQuerysetEqual(
			response.context['ultims_usuaris'],
			['<Usuari: PrimerCogn1 SegonCogn1, Nom1>']
		)


class UsuariDetailViewTest(TestCase):
	"""
	Vista que mostra informació detallada d'un usuari.
	"""

	def test_acces_vista_detall_usuari_passat(self):
		"""
		Retorna status 200 en accedir al detall d'un usuari donat d'alta amb una data_alta anterior a l'actual.
		"""
		data_alta_usu1 = timezone.now() - datetime.timedelta(days=300)
		carrec1=Carrec.objects.create(nom=u'Carrec 1', descr=u'Descripció càrrec 1')
		Usuari.objects.create(nom=u'Nom1', cognoms=u'PrimerCogn1 SegonCogn1', data_alta=data_alta_usu1, correu=u'usu1@usu.com', edat=45, carrec=carrec1)
		id_usuari=Usuari.objects.get(correu=u'usu1@usu.com').id
		response=self.client.get(reverse('usuaris:detall_usuari', args=(id_usuari,)))
		self.assertEqual(response.status_code,200)


	def test_acces_vista_detall_usuari_futur(self):
		"""
		Retorna status 200 en accedir al detall d'un usuari donat d'alta amb una data_alta anterior a l'actual.
		"""
		data_alta_usu1 = timezone.now() + datetime.timedelta(days=300)
		carrec1=Carrec.objects.create(nom=u'Carrec 1', descr=u'Descripció càrrec 1')
		Usuari.objects.create(nom=u'Nom1', cognoms=u'PrimerCogn1 SegonCogn1', data_alta=data_alta_usu1, correu=u'usu1@usu.com', edat=45, carrec=carrec1)
		id_usuari=Usuari.objects.get(correu=u'usu1@usu.com').id
		response=self.client.get(reverse('usuaris:detall_usuari', args=(id_usuari,)))
		self.assertEqual(response.status_code,200)


	def test_acces_contingut_detall_usuari_futur(self):
		"""
		Retorna status 200 en accedir al detall d'un usuari donat d'alta amb una data_alta anterior a l'actual.
		"""
		data_alta_usu1 = timezone.now() + datetime.timedelta(days=300)
		carrec1=Carrec.objects.create(nom=u'Carrec 1', descr=u'Descripció càrrec 1')
		Usuari.objects.create(nom=u'Nom1', cognoms=u'PrimerCogn1 SegonCogn1', data_alta=data_alta_usu1, correu=u'usu1@usu.com', edat=45, carrec=carrec1)
		id_usuari=Usuari.objects.get(correu=u'usu1@usu.com').id
		response=self.client.get(reverse('usuaris:detall_usuari', args=(id_usuari,)))
		self.assertContains(response, "No s'ha trobat l'usuari")


	def test_contingut_vista_usuari_passat(self):
		"""
		Retorna la informació d'un usuari si aquest té data de creació anterior a l'actual
		"""
		data_alta_usu1 = timezone.now() - datetime.timedelta(days=300)
		carrec1=Carrec.objects.create(nom=u'Carrec 1', descr=u'Descripció càrrec 1')
		usuari=Usuari.objects.create(nom=u'Nom1', cognoms=u'PrimerCogn1 SegonCogn1', data_alta=data_alta_usu1, correu=u'usu1@usu.com', edat=45, carrec=carrec1)
		response=self.client.get(reverse('usuaris:detall_usuari', args=(usuari.id,)))
		self.assertEqual(response.context['usuari'], usuari)




class LoginView(TestCase):
	"""
	Vista d'accés al portal.
	"""

	def test_login_retorna_ok(self):
		"""
		Retorna status 200 en accedir a la vista.
		"""
		response=self.client.get('/usuaris/')
		self.assertEqual(response.status_code,200)


#Crear dos usuaris amb mateix email