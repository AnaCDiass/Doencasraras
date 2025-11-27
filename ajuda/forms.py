from django import forms

class PedidoAjudaForm(forms.Form):
    nome = forms.CharField(max_length=150, label="Seu nome")
    email = forms.EmailField(label="Seu e-mail")
    mensagem = forms.CharField(widget=forms.Textarea, label="Mensagem")
