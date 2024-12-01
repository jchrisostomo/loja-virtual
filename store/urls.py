from django.urls import path
from . import views

# Define as rotas da aplicação e associa cada URL a uma função de visualização no arquivo views.py
urlpatterns = [
    path('', views.product_list, name='product_list'),  # Página inicial com a lista de produtos
    path('cart/', views.cart, name='cart'),  # Página do carrinho de compras
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # URL para adicionar um produto ao carrinho
    path('checkout/', views.checkout, name='checkout'),  # URL para finalizar a compra
]
