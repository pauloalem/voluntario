# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pais'
        db.create_table('core_pais', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['Pais'])

        # Adding model 'Estado'
        db.create_table('core_estado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sigla', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Pais'])),
        ))
        db.send_create_signal('core', ['Estado'])

        # Adding model 'Cidade'
        db.create_table('core_cidade', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Estado'])),
        ))
        db.send_create_signal('core', ['Cidade'])

        # Adding model 'Area'
        db.create_table('core_area', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['Area'])

        # Adding model 'Banco'
        db.create_table('core_banco', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('core', ['Banco'])

        # Adding model 'Usuario'
        db.create_table('core_usuario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('endereco', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('complemento', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Estado'], null=True, blank=True)),
            ('cidade', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Cidade'], null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Pais'], null=True, blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nascimento', self.gf('django.db.models.fields.DateField')(default=None, null=True, blank=True)),
            ('identificador', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, unique=True, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Usuario'])

        # Adding M2M table for field areas on 'Usuario'
        db.create_table('core_usuario_areas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('usuario', models.ForeignKey(orm['core.usuario'], null=False)),
            ('area', models.ForeignKey(orm['core.area'], null=False))
        ))
        db.create_unique('core_usuario_areas', ['usuario_id', 'area_id'])

        # Adding model 'Campanha'
        db.create_table('core_campanha', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('endereco', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('complemento', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Estado'], null=True, blank=True)),
            ('cidade', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Cidade'], null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Pais'], null=True, blank=True)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('criador', self.gf('django.db.models.fields.related.ForeignKey')(related_name='campanhas', to=orm['core.Usuario'])),
            ('data_inicio', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_fim', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Campanha'])

        # Adding model 'Voluntario'
        db.create_table('core_voluntario', (
            ('usuario_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Usuario'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('core', ['Voluntario'])

        # Adding M2M table for field participacoes on 'Voluntario'
        db.create_table('core_voluntario_participacoes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('voluntario', models.ForeignKey(orm['core.voluntario'], null=False)),
            ('campanha', models.ForeignKey(orm['core.campanha'], null=False))
        ))
        db.create_unique('core_voluntario_participacoes', ['voluntario_id', 'campanha_id'])

        # Adding model 'Beneficiario'
        db.create_table('core_beneficiario', (
            ('usuario_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Usuario'], unique=True, primary_key=True)),
            ('banco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Banco'])),
            ('conta', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('agencia', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.URLField')(default=None, max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Beneficiario'])


    def backwards(self, orm):
        # Deleting model 'Pais'
        db.delete_table('core_pais')

        # Deleting model 'Estado'
        db.delete_table('core_estado')

        # Deleting model 'Cidade'
        db.delete_table('core_cidade')

        # Deleting model 'Area'
        db.delete_table('core_area')

        # Deleting model 'Banco'
        db.delete_table('core_banco')

        # Deleting model 'Usuario'
        db.delete_table('core_usuario')

        # Removing M2M table for field areas on 'Usuario'
        db.delete_table('core_usuario_areas')

        # Deleting model 'Campanha'
        db.delete_table('core_campanha')

        # Deleting model 'Voluntario'
        db.delete_table('core_voluntario')

        # Removing M2M table for field participacoes on 'Voluntario'
        db.delete_table('core_voluntario_participacoes')

        # Deleting model 'Beneficiario'
        db.delete_table('core_beneficiario')


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
            'data_fim': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
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
            'areas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Area']", 'symmetrical': 'False'}),
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
            'participacoes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Campanha']", 'null': 'True', 'blank': 'True'}),
            'usuario_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Usuario']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['core']