from django.test import SimpleTestCase
from django.urls import reverse, resolve
from store.views import product_list, cart, add_to_cart, checkout

class URLTests(SimpleTestCase):
    def test_product_list_url(self):
        url = reverse('product_list')
        self.assertEqual(resolve(url).func, product_list)  # Função de view para listar produtos

    def test_cart_url(self):
        url = reverse('cart')
        self.assertEqual(resolve(url).func, cart)  # Função de view para exibir o carrinho

    def test_add_to_cart_url(self):
        url = reverse('add_to_cart', args=[1])  # Supondo que 1 seja o ID de um produto
        self.assertEqual(resolve(url).func, add_to_cart)  # Função de view para adicionar produto ao carrinho

    def test_checkout_url(self):
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)  # Função de view para finalizar a compra
