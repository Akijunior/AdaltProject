from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import authenticate, login, get_user_model

from .forms import UsuarioForm, PasswordResetForm
from .models import PasswordReset

User = get_user_model()

def novo_usuario(request):
    template_name = 'usuarios/novo_usuario.html'
    form = UsuarioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            usuario = form.save()
            usuario = authenticate(
                username=usuario.username, password=form.cleaned_data['password1']
            )
            login(request, usuario)
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, template_name, context)


def password_reset(request):
    template_name = 'usuarios/solicitar_nova_senha.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)


def password_reset_confirm(request, key):
    template_name = 'usuarios/password_reset_success.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.usuario, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)


# def user_profile(request):
#     return render(request, 'usuarios/show')


def editar_perfil(request):
    user = request.user
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_profile')
    else:
        form = UsuarioForm(instance=user)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})