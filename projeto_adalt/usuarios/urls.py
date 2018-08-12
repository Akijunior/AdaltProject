from django.urls import path
from .views import *
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('index/', index, name='index'),
    path('', login, {'template_name': 'usuarios/login.html'}, name='login'),
    path('sair/', logout,
         {'next_page': 'login'}, name='logout'),
    path('cadastre-se/', novo_usuario, name='novo_usuario'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('nova-senha/', password_reset, name='password_reset'),
    path('confirmar-nova-senha/<key>', password_reset_confirm, name='password_reset_confirm'),
]