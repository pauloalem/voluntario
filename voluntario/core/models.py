from django.db import models
from django.contrib.auth.models import User

class Pais(models.Model):
    nome = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=2)
    pais = models.ForeignKey(Pais)

    def __unicode__(self):
        return u'{0} ({1})'.format(self.nome, self.pais.nome)


class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return u'{0} ({1})'.format(self.nome, self.estado.sigla)


class EnderecoMixin(models.Model):
    endereco = models.TextField(null=True, blank=True, default=None)
    numero = models.IntegerField(null=True, blank=True, default=None)
    complemento = models.CharField(max_length=255, null=True, blank=True, default=None)
    estado = models.ForeignKey(Estado, null=True, blank=True, default=None)
    cidade = models.ForeignKey(Cidade, null=True, blank=True, default=None)
    pais = models.ForeignKey(Pais, null=True, blank=True, default=None)

    class Meta:
        abstract = True


class Area(models.Model):
    nome = models.CharField(max_length=255)


class Banco(models.Model):
    nome = models.CharField(max_length=255)
    numero = models.IntegerField()


class Usuario(EnderecoMixin):
    areas = models.ManyToManyField(Area)
    nome = models.CharField(max_length=255)
    identificador = models.CharField(max_length=255, unique=True, null=True, blank=True, default=None)
    email = models.EmailField()
    telefone = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='usuario/', blank=True, null=True)
    areas = models.ManyToManyField(Area)

    def __unicode__(self):
        return self.nome


class Campanha(EnderecoMixin):
    descricao = models.TextField()
    criador = models.ForeignKey(Usuario, related_name="campanhas")
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(blank=True)
    foto = models.ImageField(upload_to='campanha/', blank=True, null=True)


class Voluntario(Usuario):
    participacoes = models.ManyToManyField(Campanha,
        help_text="Campanhas que o usuario participou", null=True, blank=True)

class Beneficiario(Usuario):
    banco = models.ForeignKey(Banco)
    conta = models.CharField(max_length=255, null=True, blank=True, default=None)
    agencia = models.CharField(max_length=255, null=True, blank=True, default=None)
    site = models.URLField(null=True, blank=True, default=None)

class UsuarioPerfil(models.Model):
    usuario = models.ForeignKey(User, related_name="usuario_perfil")
    
    aceita_email = models.IntegerField(default=1)
    areas = models.ManyToManyField(Area)
