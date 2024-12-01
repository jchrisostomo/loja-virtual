import os
from pathlib import Path

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta usada para validação e criptografia no Django
SECRET_KEY = 'django-insecure-your-secret-key-here'

# Ativa o modo de depuração
DEBUG = True

# Hosts permitidos para a aplicação
ALLOWED_HOSTS = [
    'loja-virtual-hhcp.onrender.com',  # Domínio no Render
    '.render.com',  # Subdomínios no Render
    'localhost',  # Ambiente local
    '127.0.0.1',  # Loopback local
    'loja-virtual-production-95c8.up.railway.app'  # Domínio no Railway
]

# Aplicativos instalados na aplicação Django
INSTALLED_APPS = [
    'django.contrib.admin',  # Administração do Django
    'django.contrib.auth',  # Autenticação
    'django.contrib.contenttypes',  # Tipos de conteúdo
    'django.contrib.sessions',  # Sessões
    'django.contrib.messages',  # Mensagens
    'django.contrib.staticfiles',  # Arquivos estáticos
    'store',  # Aplicação customizada "store"
]

# Middleware configurados
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Segurança
    'django.contrib.sessions.middleware.SessionMiddleware',  # Gerenciamento de sessões
    'django.middleware.common.CommonMiddleware',  # Middleware comum
    'django.middleware.csrf.CsrfViewMiddleware',  # Proteção contra CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Autenticação
    'django.contrib.messages.middleware.MessageMiddleware',  # Mensagens
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Proteção contra clickjacking
]

# Configuração do arquivo de URLs principal
ROOT_URLCONF = 'config.urls'

# Configuração dos templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Backend de templates padrão
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Diretórios adicionais de templates
        'APP_DIRS': True,  # Habilita templates dentro das apps
        'OPTIONS': {
            'context_processors': [  # Processadores de contexto padrão
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuração da aplicação WSGI
WSGI_APPLICATION = 'config.wsgi.application'

# Configuração do banco de dados (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Backend do banco de dados
        'NAME': BASE_DIR / 'db.sqlite3',  # Nome do arquivo do banco
    }
}

# Validadores de senha para autenticação
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Verifica similaridade com atributos do usuário
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Exige tamanho mínimo
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Bloqueia senhas comuns
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Bloqueia senhas somente numéricas
    },
]

# Configurações de idioma e fuso horário
LANGUAGE_CODE = 'pt-br'  # Idioma padrão
TIME_ZONE = 'America/Sao_Paulo'  # Fuso horário local
USE_I18N = True  # Habilita tradução
USE_TZ = True  # Usa timezone

# Configurações de arquivos estáticos
STATIC_URL = 'static/'  # URL para arquivos estáticos
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Diretórios adicionais para arquivos estáticos

# Configuração padrão para o tipo de campo de chaves primárias
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurações de arquivos de mídia
MEDIA_URL = '/media/'  # URL para acessar arquivos de mídia
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Diretório raiz para arquivos de mídia

# Configuração do diretório de coleta de arquivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
