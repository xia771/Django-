INSTALLED_APPS = [
    # ... existing apps ...
    'rest_framework',
    'books',
] 

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static') 