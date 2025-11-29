from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from accounts.models import Paciente

User = get_user_model()


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label='E-mail')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PacienteForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, label="Senha")
    confirm_senha = forms.CharField(widget=forms.PasswordInput, label="Confirmar senha")
    doenca = forms.CharField(
        label="Doença",
        required=False,
        widget=forms.TextInput()
    )
    laudo = forms.FileField(label="Laudo médico", required=False)  # ⬅️ AQUI

    class Meta:
        model = Paciente
        fields = ['nome_completo', 'email', 'doenca', 'laudo', 'senha']

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirm_senha = cleaned_data.get("confirm_senha")

        if senha and confirm_senha and senha != confirm_senha:
            self.add_error("confirm_senha", "As senhas não coincidem.")

        return cleaned_data


class LoginForm(forms.Form):
    username_or_email = forms.CharField(
        label="Usuário ou E-mail",
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu usuário ou e-mail'})
    )
    senha = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'})
    )
