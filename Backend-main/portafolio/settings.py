from pathlib import Path
from decouple import config
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key")
DEBUG = True

ALLOWED_HOSTS = [
    "portfolio-pijl.onrender.com",
    "dainty-starship-d1371d.netlify.app",
    "localhost",
]

# URLConf
ROOT_URLCONF = 'portafolio.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",  # 👈
]

# Middleware
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # 👈 debe ir primero
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# CORS
CORS_ALLOWED_ORIGINS = [
    "https://dainty-starship-d1371d.netlify.app",
]
CSRF_TRUSTED_ORIGINS = [
    "https://dainty-starship-d1371d.netlify.app",
]
CORS_ALLOW_HEADERS = ["content-type","authorization"]
CORS_ALLOW_METHODS = ["GET", "POST", "OPTIONS"]
CORS_EXPOSE_HEADERS = ["Content-Type"]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = False

# Emails (Gmail con contraseña de aplicación)

BREVO_API_KEY = config("BREVO_API_KEY")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")

# Archivos estáticos
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
