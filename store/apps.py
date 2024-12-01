from django.apps import AppConfig

# Configuração da aplicação Django chamada "store"
class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Define o tipo de campo padrão para chaves primárias
    name = 'store'  # Nome da aplicação (deve coincidir com o nome do diretório da app)
