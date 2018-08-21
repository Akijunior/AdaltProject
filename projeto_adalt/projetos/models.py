from django.db import models
from django.conf import settings

# Create your models here.
class Projeto(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='projetos',
                             on_delete=models.CASCADE)
    nome = models.CharField(max_length=500)
    setor = models.CharField(max_length=500)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.nome
