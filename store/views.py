from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Cart

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.total for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, 'Produto adicionado ao carrinho!')
    return redirect('product_list')

@login_required
def checkout(request):
    Cart.objects.filter(user=request.user).delete()
    messages.success(request, 'Pedido realizado com sucesso!')
    return redirect('product_list')