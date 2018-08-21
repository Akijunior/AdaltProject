from django.urls import path
from .views import *

urlpatterns = [
    path('criar_projeto', novo_projeto, name='novo_projeto'),
]
