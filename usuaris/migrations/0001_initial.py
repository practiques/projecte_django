# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carrec'
        db.create_table(u'usuaris_carrec', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal(u'usuaris', ['Carrec'])

        # Adding model 'Usuari'
        db.create_table(u'usuaris_usuari', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('cognoms', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('data_alta', self.gf('django.db.models.fields.DateTimeField')()),
            ('correu', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('carrec', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['usuaris.Carrec'])),
        ))
        db.send_create_signal(u'usuaris', ['Usuari'])


    def backwards(self, orm):
        # Deleting model 'Carrec'
        db.delete_table(u'usuaris_carrec')

        # Deleting model 'Usuari'
        db.delete_table(u'usuaris_usuari')


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
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['usuaris']