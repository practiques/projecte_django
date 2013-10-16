# -*- encoding: utf-8 -*-
from django.db import models
import math
import random
import bcrypt
import hashlib

class Carrec(models.Model):
	nom=models.CharField(max_length=30)
	descr=models.CharField(max_length=70)
	def __str__(self):
		return self.nom

class Pais(models.Model):		#Ho implemento com a nova classe per si vul afegir alguna informació en el futur.
	nom=models.CharField(max_length=50)
	def __str__(self):
		return self.nom

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
		contra_hash=hashlib.sha512(repr(contra)+','+repr(contra_salt)).hexdigest();
		return contra_hash


class Usuari(models.Model):

	nom=models.CharField(max_length=30)
	cognoms=models.CharField(max_length=60)
	data_alta=models.DateTimeField()
	correu=models.EmailField()
	# L'edat adquireix valor aleatori amb la migració (entre 0 i 999)
	edat=models.IntegerField(default=random.randrange(0,999))
	#contra=models.CharField(max_length=60,default='contrasenya') #Esborrem aquest camp per completar la migració.
	contra_salt = models.CharField(max_length=8, null=True)
	contra_hash = models.CharField(max_length=40, null=True)
	#contra_salt=models.TextField(default=Contrasenya.generar_salt())
	#contra_hash=models.TextField(default=Contrasenya.generar_hash(contra,contra_salt))
	ciutat=models.ForeignKey(Ciutat,null=True)	
	carrec=models.ForeignKey(Carrec)
	def __str__(self):
		return self.cognoms+", "+self.nom




