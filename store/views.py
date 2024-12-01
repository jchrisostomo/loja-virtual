from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Cart

# Exibe a lista de produtos disponíveis na loja
def product_list(request):
    products = Product.objects.all()  # Obtém todos os produtos cadastrados no banco de dados
    return render(request, 'store/product_list.html', {'products': products})  # Renderiza a página com a lista de produtos

# Exibe o carrinho de compras do usuário
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)  # Filtra os itens do carrinho pertencentes ao usuário logado
    total = sum(item.total for item in cart_items)  # Calcula o valor total do carrinho
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})  # Renderiza a página do carrinho

# Adiciona um produto ao carrinho do usuário
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)  # Obtém o produto pelo ID
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)  # Busca ou cria um item no carrinho para o produto

    if not created:  # Se o item já existia, incrementa a quantidade
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, 'Produto adicionado ao carrinho!')  # Exibe uma mensagem de sucesso
    return redirect('product_list')  # Redireciona para a lista de produtos

# Finaliza a compra, limpando o carrinho do usuário (requer login)
def checkout(request):
    Cart.objects.filter(user=request.user).delete()  # Remove todos os itens do carrinho do usuário logado
    messages.success(request, 'Pedido realizado com sucesso!')  # Exibe uma mensagem de sucesso
    return redirect('product_list')  # Redireciona para a lista de produtos
