from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=200)

class Contato(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200, blank=True)
    telefone = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True)
    data = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

