from django.db import models
from django.conf import settings

AUTH_USER_MODEL = 'accounts.CustomUser'
# advanced_features_and_sercurity/LibraryProject/bookshelf/settings.py
user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts', # Add this file
]

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

AUTH_USER_MODEL = 'accounts.CustomUser'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# LibraryProject/settings.py

Debug = False 

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Optional: Add CSP middleware for enhanced security
INSTALLED_APPS += ['csp']
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',  # Add this line
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CPS_DEFAULT_SRC = ("'self'",)
CPS_SCRIPT_SRC = ("'self'", "https://trusted.cdn.com")
CPS_STYLE_SRC = ("'self'", "https://trusted.cdn.com")

# LibraryProject/settings.py

# Redirect all HTTP traffic to HTTPS
SECURE_SSL_REDIRECT = True

# Enforce HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000  # One year in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True # Apply HSTS to all subdomains HSTS list
SECURE_HSTS_PRELOAD = True # Allow site to be included in browsers' HSTS preload list

# Secure cookies
SESSION_COOKIE_SECURE = True # Ensure session cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True # Ensure CSRF cookies are only sent over HTTPS

# Secure headers
X_FRAME_OPTIONS = 'DENY' # Prevent clickjacking by disallowing the site to be framed
SECURE_CONTENT_TYPE_NOSNIFF = True # Prevent MIME type sniffing
SECURE_BROWSER_XSS_FILTER = True # Enable the browser's XSS filtering and prevent reflected XSS attacks

# Optional: Set ALLOWED_HOSTS for production
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
