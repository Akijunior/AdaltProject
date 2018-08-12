from django import forms
from django.contrib.auth import get_user_model

from core.mail import send_mail_template
from core.utils import generate_hash_key

from usuarios.models import *

User = get_user_model()

class UsuarioForm(forms.ModelForm):


    senha1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    senha2 = forms.CharField(
        label='Confirmação de Senha', widget=forms.PasswordInput
    )

    def clean_password2(self):
        senha1 = self.cleaned_data.get("senha1")
        senha2 = self.cleaned_data.get("senha2")
        if senha1 and senha2 and senha1 != senha2:
            raise forms.ValidationError('A confirmação não está correta')
        return senha2

    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data['senha1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = Usuario
        fields = ('nome_completo', 'email', 'nome_empresa', 'especialidade', 'senha1', 'senha2')




class PasswordResetForm(forms.Form):


    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError('Não foi encontrado nenhum usuário com esse e-mail.')

    def save(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.email)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        template_name = 'account/password_reset_mail.html'
        subject = 'Criar nova senha de acesso para o Active Gears'
        context = {
            'reset':reset
        }
        send_mail_template(subject, template_name, context, [user.email])