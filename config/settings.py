INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts',
    'restaurants',
    'orders',
]
AUTH_USER_MODEL = 'accounts.User'
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'

