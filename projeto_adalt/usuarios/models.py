import re

from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, UserManager
from django.core import validators
from django.db import models

from django.conf import settings

class Usuario(AbstractBaseUser, PermissionsMixin):
    TIPOS_ESPECIALIDADES = (
        (0, 'Administração'),
        (1, 'Análise de desempenho'),
        (2, 'Desenvolvimento de software'),
        (3, 'Design'),
        (4, 'Gerenciamento de equipe'),
        (5, 'Gerenciamento de projeto'),
        (6, 'Programação'),
    )

    nome_completo = models.CharField('Nome coompleto do usuário', max_length=30, unique=True,
                                validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                                                      'O nome do usuário só deve conter letras',
                                                                      'invalid')])
    email = models.EmailField('E-mail', unique=True)
    nome_empresa = models.CharField('Nome da empresa a qual pertence', max_length=100, blank=True)
    especialidade = models.IntegerField('Principal especialidade profissional', choices=TIPOS_ESPECIALIDADES, default=0, blank=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome_completo']

    def __str__(self):
        return self.nome_completo or self.email

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class PasswordReset(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='resets',
                             on_delete=models.CASCADE)
    chave = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

    def __str__(self):
        return '{0} em {1}'.format(self.usuario, self.created_at)

    class Meta:
        verbose_name = 'Nova senha.'
        verbose_name_plural = 'Novas senhas.'
        ordering = ['-created_at']