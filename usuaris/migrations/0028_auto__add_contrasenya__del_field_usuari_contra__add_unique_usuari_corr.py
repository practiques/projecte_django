# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contrasenya'
        db.create_table(u'usuaris_contrasenya', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'usuaris', ['Contrasenya'])

        # Deleting field 'Usuari.contra'
        db.delete_column(u'usuaris_usuari', 'contra')

        # Adding unique constraint on 'Usuari', fields ['correu']
        db.create_unique(u'usuaris_usuari', ['correu'])


        # Changing field 'Usuari.contra_salt'
        db.alter_column(u'usuaris_usuari', 'contra_salt', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

    def backwards(self, orm):
        # Removing unique constraint on 'Usuari', fields ['correu']
        db.delete_unique(u'usuaris_usuari', ['correu'])

        # Deleting model 'Contrasenya'
        db.delete_table(u'usuaris_contrasenya')

        # Adding field 'Usuari.contra'
        db.add_column(u'usuaris_usuari', 'contra',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True),
                      keep_default=False)


        # Changing field 'Usuari.contra_salt'
        db.alter_column(u'usuaris_usuari', 'contra_salt', self.gf('django.db.models.fields.CharField')(max_length=8, null=True))

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
        u'usuaris.contrasenya': {
            'Meta': {'object_name': 'Contrasenya'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'contra_hash': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'contra_salt': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'correu': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'data_alta': ('django.db.models.fields.DateTimeField', [], {}),
            'edat': ('django.db.models.fields.IntegerField', [], {'default': '735'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['usuaris']