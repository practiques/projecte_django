# -*- encoding: utf-8 -*-
from django.http import HttpResponse
from django.contrib import admin
from usuaris.models import *
from django.forms import ModelForm
from django import forms
from django.http import Http404


class UsuariForm(ModelForm):
	raw_password=forms.CharField(required=False)
	contra_hash=forms.CharField(
		required=False,
		widget=forms.Textarea(attrs={'rows': 5, 'cols': 100, 'readonly':'readonly'})
		)


	class Meta:
		model=Usuari
		fields=['nom','cognoms','correu','edat','ciutat','carrec','data_alta','raw_password', 'contra_hash']

	def clean(self):
		correu_form=self.cleaned_data['correu']
		#try:
		#usuari=Usuari.objects.get(correu=correu_form) #Comprovem si existeix un usuari amb aquest correu.
		#raise forms.ValidationError("Ja existeix un usuari amb aquest correu.")
		#except Usuari.DoesNotExist:
		#cleaned_data = super(UsuariForm, self).clean()
		if not self.cleaned_data['contra_hash'] and not self.cleaned_data['raw_password']:
			raise forms.ValidationError("Aquest usuari encara no disposa de contrasenya.")
		else:
			return self.cleaned_data

	def save(self,commit=True):
		obj=super(UsuariForm, self).save(commit=False)
		if self.cleaned_data['raw_password']:
			raw_pass=self.cleaned_data['raw_password']
			obj.contra_salt=Contrasenya.generar_salt()
			obj.contra_hash=Contrasenya.generar_hash(raw_pass,obj.contra_salt)
		if commit:
			obj.save()
		return obj


class UsuariAdmin(admin.ModelAdmin):
	fieldsets=[
		("Informació de l'usuari",	{'fields':['nom','cognoms','correu', 'edat', 'ciutat', 'contra_hash', 'raw_password']}),
		("Relació amb l'empresa",	{'fields':['carrec','data_alta']}),
	]
	form=UsuariForm


"""
	def save(self, request, obj, form, change):
		from django.http import HttpResponse
		return HttpResponse(str(form['contra']))
        #obj.save()
"""

admin.site.register(Usuari,UsuariAdmin)
admin.site.register(Carrec)
admin.site.register(Ciutat)
admin.site.register(Pais)
admin.site.register(Comunitat)