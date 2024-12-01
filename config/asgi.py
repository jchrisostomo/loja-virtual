import os
from django.core.asgi import get_asgi_application

# Define a configuração padrão do Django para o ambiente
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Obtém a aplicação ASGI do Django
application = get_asgi_application()
