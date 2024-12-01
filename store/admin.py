from django.contrib import admin
from .models import Category, Product, Cart

# Configurações de exibição para o modelo Category no Django Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']  # Define as colunas exibidas na lista de categorias
    search_fields = ['name']  # Permite a busca por nome no Django Admin

# Configurações de exibição para o modelo Product no Django Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'stock']  # Define as colunas exibidas na lista de produtos
    list_filter = ['category']  # Adiciona filtro por categoria no Django Admin
    search_fields = ['name', 'description']  # Permite a busca por nome e descrição dos produtos

# Configurações de exibição para o modelo Cart no Django Admin
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'created_at']  # Define as colunas exibidas na lista de itens do carrinho
    list_filter = ['user']  # Adiciona filtro por usuário no Django Admin
