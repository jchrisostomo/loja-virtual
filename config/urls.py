from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Define as rotas principais do projeto
urlpatterns = [
    path('admin/', admin.site.urls),  # URL para acessar o painel de administração do Django
    path('', include('store.urls')),  # Inclui as rotas definidas na aplicação 'store'
] 

# Adiciona configuração para servir arquivos de mídia durante o desenvolvimento
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
