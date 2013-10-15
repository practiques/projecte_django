# -*- encoding: utf-8 -*-
from django.db import models
import math
import random

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

class Usuari(models.Model):
	nom=models.CharField(max_length=30)
	cognoms=models.CharField(max_length=60)
	data_alta=models.DateTimeField()
	correu=models.EmailField()
	# L'edat adquireix valor aleatori amb la migració (entre 0 i 999)
	edat=models.IntegerField(default=random.randrange(0,999))
	ciutat=models.ForeignKey(Ciutat,null=True)	#Pot ser null ja que és l'últim camp que creo i ja existeixen registres anteriors.
	carrec=models.ForeignKey(Carrec)
	def __str__(self):
		return self.cognoms+", "+self.nom

