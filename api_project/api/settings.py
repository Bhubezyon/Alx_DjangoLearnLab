INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken', # Enables token support
    'api'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated', # Default: restrict all views
    ],
}