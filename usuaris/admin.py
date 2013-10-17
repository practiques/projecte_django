# -*- encoding: utf-8 -*-
from django.contrib import admin
from usuaris.models import *

class UsuariAdmin(admin.ModelAdmin):
	fieldsets=[
		("Informació de l'usuari",	{'fields':['nom','cognoms','correu', 'ciutat', 'contra']}),
		("Relació amb l'empresa",	{'fields':['carrec','data_alta']}),
	]

admin.site.register(Usuari,UsuariAdmin)
admin.site.register(Carrec)
admin.site.register(Ciutat)
admin.site.register(Pais)
admin.site.register(Comunitat)