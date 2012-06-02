# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Campanha.nome'
        db.add_column('core_campanha', 'nome',
                      self.gf('django.db.models.fields.CharField')(default='Camapanha', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Campanha.nome'
        db.delete_column('core_campanha', 'nome')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.area': {
            'Meta': {'object_name': 'Area'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.banco': {
            'Meta': {'object_name': 'Banco'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numero': ('django.db.models.fields.IntegerField', [], {})
        },
        'core.beneficiario': {
            'Meta': {'object_name': 'Beneficiario', '_ormbases': ['core.Usuario']},
            'agencia': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'banco': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Banco']"}),
            'conta': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'usuario_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Usuario']", 'unique': 'True', 'primary_key': 'True'})
        },
        'core.campanha': {
            'Meta': {'object_name': 'Campanha'},
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['core.Cidade']", 'null': 'True', 'blank': 'True'}),
            'complemento': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'criador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'campanhas'", 'to': "orm['core.Usuario']"}),
            'data_fim': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'data_inicio': ('django.db.models.fields.DateTimeField', [], {}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'endereco': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['core.Estado']", 'null': 'True', 'blank': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "'Camapanha'", 'max_length': '30'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['core.Pais']", 'null': 'True', 'blank': 'True'})
        },
        'core.cidade': {
            'Meta': {'object_name': 'Cidade'},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Estado']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.estado': {
            'Meta': {'object_name': 'Estado'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Pais']"}),
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'core.pais': {
            'Meta': {'object_name': 'Pais'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'aceita_email': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'areas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Area']", 'symmetrical': 'False'}),
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['core.Cidade']", 'null': 'True', 'blank': 'True'}),
            'complemento': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'endereco': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['core.Estado']", 'null': 'True', 'blank': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificador': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['core.Pais']", 'null': 'True', 'blank': 'True'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'usuario'", 'unique': 'True', 'to': "orm['auth.User']"})
        },
        'core.voluntario': {
            'Meta': {'object_name': 'Voluntario', '_ormbases': ['core.Usuario']},
            'nascimento': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'participacoes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Campanha']", 'null': 'True', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'usuario_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Usuario']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['core']