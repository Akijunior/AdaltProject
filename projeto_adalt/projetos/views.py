from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projetos.forms import ProjetoForm
from .models import *
from django.shortcuts import redirect

# Create your views here.
@login_required
def novo_projeto(request):
    template_name = 'novo_projeto.html'
    form = ProjetoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            projeto = Projeto()
            projeto.nome = request.POST.get('nome', '')
            projeto.setor = request.POST.get('setor', '')
            projeto.descricao = request.POST.get('descricao', '')
            projeto.usuario = request.user
            projeto.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, template_name, context)