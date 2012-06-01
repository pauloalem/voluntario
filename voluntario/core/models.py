from django.db import models

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


class Categoria(models.Model):
    nome = models.CharField(max_length=255)


class Area(models.Model):
    nome = models.CharField(max_length=255, unique=True)


class Banco(models.Model):
    nome = models.CharField(max_length=255)
    numero = models.IntegerField()

class Usuario(EnderecoMixin):
    nome = models.CharField(max_length=255)
    nascimento = models.DateField(null=True, blank=True, default=None)
    identificador = models.CharField(max_length=255, unique=True, null=True, blank=True, default=None)
    email = models.EmailField()
    telefone = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='usuario/', blank=True, null=True)

    def __unicode__(self):
        return self.nome


class Campanha(EnderecoMixin):
    descricao = models.TextField()
    criador = models.ForeignKey(Usuario, related_name="campanhas")
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    areas_interesse = models.ManyToManyField(Area)
    categorias = models.ManyToManyField(Categoria)
    foto = models.ImageField(upload_to='campanha/', blank=True, null=True)


class Voluntario(Usuario):
    areas_interesse = models.ManyToManyField(Area)
    categorias = models.ManyToManyField(Categoria)
    participacoes = models.ManyToManyField(Campanha,
        help_text="Campanhas que o usuario participou")


class Beneficiario(Usuario):
    banco = models.ForeignKey(Banco)
    conta = models.CharField(max_length=255, null=True, blank=True, default=None)
    agencia = models.CharField(max_length=255, null=True, blank=True, default=None)
    site = models.URLField(null=True, blank=True, default=None)
    area_atuacao = models.ManyToManyField(Area)
    categoria = models.ManyToManyField(Categoria)