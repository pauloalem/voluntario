# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        orm['core.Area'].objects.create(nome="Educação")
        orm['core.Area'].objects.create(nome="Saúde")
        orm['core.Area'].objects.create(nome="Meio Ambiente")
        orm['core.Area'].objects.create(nome="Esporte/Artes")
        orm['core.Area'].objects.create(nome="Animais")
        orm['core.Area'].objects.create(nome="Serviço Social")

    def backwards(self, orm):
        orm['core.Area'].objects.all().delete()
        "Write your backwards methods here."

    models = {
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
            'areas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Area']", 'symmetrical': 'False'}),
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
            'data_fim': ('django.db.models.fields.DateTimeField', [], {}),
            'data_inicio': ('django.db.models.fields.DateTimeField', [], {}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'endereco': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['core.Estado']", 'null': 'True', 'blank': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['core.Cidade']", 'null': 'True', 'blank': 'True'}),
            'complemento': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'endereco': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['core.Estado']", 'null': 'True', 'blank': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificador': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'nascimento': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['core.Pais']", 'null': 'True', 'blank': 'True'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.voluntario': {
            'Meta': {'object_name': 'Voluntario', '_ormbases': ['core.Usuario']},
            'areas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Area']", 'symmetrical': 'False'}),
            'participacoes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Campanha']", 'symmetrical': 'False'}),
            'usuario_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Usuario']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['core']
    symmetrical = True
