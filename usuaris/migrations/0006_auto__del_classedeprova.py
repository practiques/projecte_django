# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ClasseDeProva'
        db.delete_table(u'usuaris_classedeprova')


    def backwards(self, orm):
        # Adding model 'ClasseDeProva'
        db.create_table(u'usuaris_classedeprova', (
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=30)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'usuaris', ['ClasseDeProva'])


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
            'prova': ('django.db.models.fields.CharField', [], {'default': "'prova'", 'max_length': '60', 'null': 'True'}),
            'prova2': ('django.db.models.fields.CharField', [], {'default': "'prova2'", 'max_length': '60'})
        }
    }

    complete_apps = ['usuaris']