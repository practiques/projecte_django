# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Usuari.ciutat'
        db.add_column(u'usuaris_usuari', 'ciutat',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['usuaris.Ciutat'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Usuari.ciutat'
        db.delete_column(u'usuaris_usuari', 'ciutat_id')


    models = {
        u'usuaris.carrec': {
            'Meta': {'object_name': 'Carrec'},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'usuaris.ciutat': {
            'Meta': {'object_name': 'Ciutat'},
            'comunitat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['usuaris.Comunitat']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'usuaris.comunitat': {
            'Meta': {'object_name': 'Comunitat'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['usuaris.Pais']"})
        },
        u'usuaris.pais': {
            'Meta': {'object_name': 'Pais'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'usuaris.usuari': {
            'Meta': {'object_name': 'Usuari'},
            'carrec': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['usuaris.Carrec']"}),
            'ciutat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['usuaris.Ciutat']", 'null': 'True'}),
            'cognoms': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'correu': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'data_alta': ('django.db.models.fields.DateTimeField', [], {}),
            'edat': ('django.db.models.fields.IntegerField', [], {'default': '754'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['usuaris']