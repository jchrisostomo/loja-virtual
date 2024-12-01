from django.urls import reverse
from django.test import TestCase
from store.models import Category, Product  # Corrigir para 'Category' e 'Product'

class StoreViewTests(TestCase):
    def test_product_list_view(self):
        category = Category.objects.create(name="Categoria C", description="Descrição da Categoria C")  # Alterar para 'Category'
        Product.objects.create(
            name="Produto B", 
            description="Descrição do Produto B", 
            price=150.0, 
            image="produto-b.jpg", 
            stock=5,
            category=category  # Alterar para 'Category'
        )
        url = reverse('product_list')  # URL da view
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Produto B")
