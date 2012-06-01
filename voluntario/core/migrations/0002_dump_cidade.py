# -*- coding: utf-8 -*-
import os
from south.db import db
from south.v2 import SchemaMigration
from voluntario.core.models import Pais, Estado, Cidade

class Migration(SchemaMigration):

    def forwards(self, orm):
        dump_data = open(os.path.join(os.path.dirname(__file__), 'municipios.sql'), 'r')
        db.execute(dump_data.read())

    def backwards(self, orm):
        brasil = Pais.objects.get(nome='Brasil')
        estados_brasileiros = Estado.objects.filter(pais=brasil)
        cidades_brasileiras = Cidade.objects.filter(estado__in=estados_brasileiros)
        cidades_brasileiras.delete()
        estados_brasileiros.delete()
        brasil.delete()