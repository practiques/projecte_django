# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Usuari.prova'
        db.add_column(u'usuaris_usuari', 'prova',
                      self.gf('django.db.models.fields.CharField')(max_length=60, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Usuari.prova'
        db.delete_column(u'usuaris_usuari', 'prova')


    models = {
        u'usuaris.carrec': {
            'Meta': {'object_name': 'Carrec'},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'usuaris.usuari': {
            'Meta': {'object_name': 'Usuari'},
            'carrec': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['usuaris.Carrec']"}),
            'cognoms': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'correu': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'data_alta': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'prova': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'})
        }
    }

    complete_apps = ['usuaris']