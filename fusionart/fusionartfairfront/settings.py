
import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = BASE_DIR / ".env"
load_dotenv(dotenv_path)




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-+s^t$3&$9cbjdmygk4gcz*vk(wuw!zdu3i^e)op=zmulg3*pih'
SECRET_KEY = os.environ['SECRET_KEY']
WEBSITE_HOSTNAME = os.environ.get('WEBSITE_HOSTNAME', None)
DEBUG = WEBSITE_HOSTNAME == None


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



ALLOWED_HOSTS = ['*'] if DEBUG else ['localhost']

if not DEBUG:
    CSRF_TRUSTED_ORIGINS = ['localhost']



CORS_ALLOWED_ORIGINS =['http://localhost:8000']


CSRF_TRUSTED_ORIGINS =[
    'http://localhost:8080',
    'http://localhost:8000',

]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fusionartfair',
    'corsheaders',

]





MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fusionartfairfront.urls'

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

WSGI_APPLICATION = 'fusionartfairfront.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {

   'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
    


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "registration/static"),
# ]


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = "/fusionartfair/static/"
MEDIA_URL= "/fusionartfair/media/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]



EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
