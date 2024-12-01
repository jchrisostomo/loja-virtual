from django.db import models
from django.contrib.auth.models import User

# Modelo para representar uma categoria de produtos
class Category(models.Model):
    name = models.CharField(max_length=100)  # Nome da categoria
    description = models.TextField(blank=True)  # Descrição opcional da categoria

    class Meta:
        verbose_name_plural = 'Categories'  # Nome plural para exibição no Django Admin

    def __str__(self):
        return self.name  # Representação em texto da categoria

# Modelo para representar um produto na loja
class Product(models.Model):
    name = models.CharField(max_length=200)  # Nome do produto
    description = models.TextField()  # Descrição do produto
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Categoria associada ao produto
    image = models.ImageField(upload_to='products/', blank=True)  # Imagem opcional do produto
    stock = models.IntegerField(default=0)  # Quantidade em estoque
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação do produto

    def __str__(self):
        return self.name  # Representação em texto do produto

# Modelo para representar itens no carrinho de compras
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuário dono do carrinho
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Produto adicionado ao carrinho
    quantity = models.IntegerField(default=1)  # Quantidade do produto no carrinho
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação do item no carrinho

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"  # Representação em texto do item no carrinho

    # Propriedade que calcula o total do item no carrinho (preço x quantidade)
    @property
    def total(self):
        return self.quantity * self.product.price
