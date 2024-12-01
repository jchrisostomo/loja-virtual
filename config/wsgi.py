import os
from django.core.wsgi import get_wsgi_application

# Define a configuração padrão para o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Cria a aplicação WSGI que será usada pelo servidor para servir o projeto Django
application = get_wsgi_application()