from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Category, Product, Cart

class StoreModelTests(TestCase):

    def setUp(self):
        # Criação de um usuário para testes
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
    def test_create_category(self):
        # Teste para criar uma categoria
        category = Category.objects.create(name="Categoria A", description="Descrição da Categoria A")
        self.assertEqual(category.name, "Categoria A")
        self.assertEqual(category.description, "Descrição da Categoria A")
    
    def test_create_product(self):
        # Teste para criar um produto
        category = Category.objects.create(name="Categoria B", description="Descrição da Categoria B")
        product = Product.objects.create(
            name="Produto A", 
            description="Descrição do Produto A", 
            price=100.0, 
            category=category, 
            image="produto-a.jpg", 
            stock=10
        )
        self.assertEqual(product.name, "Produto A")
        self.assertEqual(product.price, 100.0)
        self.assertEqual(product.category.name, "Categoria B")
    
    def test_add_to_cart(self):
        # Teste para adicionar um produto ao carrinho
        category = Category.objects.create(name="Categoria C", description="Descrição da Categoria C")
        product = Product.objects.create(
            name="Produto B", 
            description="Descrição do Produto B", 
            price=150.0, 
            category=category, 
            image="produto-b.jpg", 
            stock=5
        )
        # Adiciona o produto ao carrinho
        cart_item = Cart.objects.create(user=self.user, product=product, quantity=2)
        
        # Verifica se o item foi adicionado corretamente ao carrinho
        self.assertEqual(cart_item.user, self.user)
        self.assertEqual(cart_item.product, product)
        self.assertEqual(cart_item.quantity, 2)
        self.assertEqual(cart_item.total, 300.0)  # 150.0 * 2
    
    def test_cart_total(self):
        # Teste para verificar o total do carrinho
        category = Category.objects.create(name="Categoria D", description="Descrição da Categoria D")
        product1 = Product.objects.create(
            name="Produto C", 
            description="Descrição do Produto C", 
            price=100.0, 
            category=category, 
            image="produto-c.jpg", 
            stock=10
        )
        product2 = Product.objects.create(
            name="Produto D", 
            description="Descrição do Produto D", 
            price=50.0, 
            category=category, 
            image="produto-d.jpg", 
            stock=10
        )
        Cart.objects.create(user=self.user, product=product1, quantity=2)
        Cart.objects.create(user=self.user, product=product2, quantity=3)

        # Calcula o total do carrinho
        cart_items = Cart.objects.filter(user=self.user)
        total = sum(item.total for item in cart_items)
        
        self.assertEqual(total, 350.0)  # (100.0 * 2) + (50.0 * 3)
