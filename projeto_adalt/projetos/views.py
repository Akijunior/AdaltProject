from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projetos.forms import ProjetoForm

# Create your views here.
@login_required
def novo_projeto(request):
    template_name = 'novo_projeto.html'
    form = ProjetoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            projeto = form.save()
            login(request, usuario)
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, template_name, context)