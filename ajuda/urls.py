from django.urls import path
from . import views

urlpatterns = [
    path('', views.ajuda_redirect, name='ajuda'),
    path('novo/', views.PedidoAjudaCreateView.as_view(), name='pedido-ajuda'),
    path('obrigado/', views.pedido_ajuda_obrigado, name='pedido-ajuda-obrigado'),
]
