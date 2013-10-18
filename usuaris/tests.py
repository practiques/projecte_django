"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import timezone
from usuaris.models import *

class UsuarisMethodTests(TestCase):

    def test_usuari_creat_recentment_amb_data_futura(self):
        time = timezone.now() + datetime.timedelta(days=30)
        usuari_futur = Usuari(nom='Nom',cognoms='Cognom1 Cognom2',data_alta=time,correu='r@r.com',edat=27)
        self.assertEqual(usuari_futur.creat_recentment(), False)

	def test_usuari_creat_recentment_amb_data_darrer_dia(self):
		time = timezone.now() - datetime.timedelta(days=1)
		usuari_futur = Usuari(nom='Nom',cognoms='Cognom1 Cognom2',data_alta=time,correu='r@r.com',edat=27)
		self.assertEqual(usuari_futur.creat_recentment(), True)
