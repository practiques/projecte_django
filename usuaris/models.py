# -*- encoding: utf-8 -*-
from django.db import models
import math
import random
#import bcrypt
import hashlib
from django.utils import timezone
import datetime

class Carrec(models.Model):
	nom=models.CharField(max_length=30)
	descr=models.CharField(max_length=70)
	def __str__(self):
		return self.nom

class Pais(models.Model):		#Ho implemento com a nova classe per si vul afegir alguna informació en el futur.
	nom=models.CharField(max_length=50)
	def __str__(self):
		return self.nom

""
class Comunitat(models.Model):
	nom=models.CharField(max_length=50)
	pais=models.ForeignKey(Pais)
	def __str__(self):
		return self.nom

class Ciutat(models.Model):
	nom=models.CharField(max_length=50)
	comunitat=models.ForeignKey(Comunitat)
	def __str__(self):
		return self.nom


class Contrasenya(models.Model):

	alfabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	@classmethod
	def generar_salt(cls):
		salt=''.join(random.choice(cls.alfabet) for i in range(16)) 
		return salt

	@classmethod
	def generar_hash(cls,contra,contra_salt):
		contra_hash=hashlib.sha512(contra+','+contra_salt).hexdigest();
		return contra_hash


class Usuari(models.Model):

	nom=models.CharField(max_length=30)
	cognoms=models.CharField(max_length=60)
	data_alta=models.DateTimeField()
	correu=models.EmailField(unique=True)
	# L'edat adquireix valor aleatori amb la migració (entre 0 i 999)
	edat=models.IntegerField(default=random.randrange(0,999))
	
	#Afegim els camps "salt" i "hash" tot indicant un valor per defecte per poder fer la migració.
	#contra_salt=models.TextField(default=Contrasenya.generar_salt())
	#contra_hash=models.TextField(default=Contrasenya.generar_hash(contra,contra_salt))

	#Una vegada hem migrat, esborrem el la contrasenya "raw" per completar la migració.
	#contra=models.CharField(max_length=60,default='contrasenya') 

	contra_salt = models.CharField(max_length=20, null=True)
	contra_hash = models.TextField(null=True)
	
	ciutat=models.ForeignKey(Ciutat,null=True)	
	carrec=models.ForeignKey(Carrec)
	
	def creat_recentment(self):
		return timezone.now() > self.data_alta >= timezone.now() - datetime.timedelta(days=1)

	def any_naixement(self):
		return timezone.now().year - self.edat

	def __str__(self):
		return self.cognoms+", "+self.nom



