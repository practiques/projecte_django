# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Usuari.contra_hash'
        db.add_column(u'usuaris_usuari', 'contra_hash',
                      self.gf('django.db.models.fields.TextField')(default='b5fff34ee0d33ad36a974fe938670a1b39fab8bb91cd1dcd90ad099ddc9abda76f7c41be2756bdd527ed43c8780890c15ac220e8786a5a10e0c7f622b7991f6d'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Usuari.contra_hash'
        db.delete_column(u'usuaris_usuari', 'contra_hash')


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
            'contra': ('django.db.models.fields.CharField', [], {'default': "'contrasenya'", 'max_length': '60'}),
            'contra_hash': ('django.db.models.fields.TextField', [], {'default': "'b5fff34ee0d33ad36a974fe938670a1b39fab8bb91cd1dcd90ad099ddc9abda76f7c41be2756bdd527ed43c8780890c15ac220e8786a5a10e0c7f622b7991f6d'"}),
            'contra_salt': ('django.db.models.fields.TextField', [], {'default': "'QlXlraM0aakzsRaJ'"}),
            'correu': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'data_alta': ('django.db.models.fields.DateTimeField', [], {}),
            'edat': ('django.db.models.fields.IntegerField', [], {'default': '751'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['usuaris']