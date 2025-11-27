from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import PedidoAjuda

@method_decorator(login_required, name='dispatch')
class PedidoAjudaCreateView(CreateView):
    model = PedidoAjuda
    fields = ['titulo', 'descricao']
    template_name = 'ajuda/form.html'
    success_url = reverse_lazy('pedido-ajuda-obrigado')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

def pedido_ajuda_obrigado(request):
    return render(request, 'ajuda/obrigado.html')

def ajuda_redirect(request):
    if request.user.is_authenticated:
        return redirect('pedido-ajuda')  # vai para o formulário
    return render(request, 'ajuda/precisa_login.html')  # mostra a tela pedindo login
