"""
Django settings for bookr project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from configurations import Configuration, values
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
class Dev(Configuration):
    BASE_DIR = Path(__file__).resolve().parent.parent
    SECRET_KEY = "django-insecure-c!ed4dqj0ous$i*%zf&xxf*skpgkey6%$ld-pz6s^_k6w#eo7&"
    DEBUG = values.BooleanValue(True)
    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!

    # SECURITY WARNING: don't run with debug turned on in production!

    ALLOWED_HOSTS = values.ListValue([])

    # Application definition

    INSTALLED_APPS = [
        "bookr_admin.apps.BookrAdminConfig",
        "django.contrib.sites",
        "reviews.adminconfig.ReviewsAdminConfig",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "rest_framework",
        "rest_framework.authtoken",
        "reviews",
        "filter_demo",
        "book_management",
        "bookr_test",
        "debug_toolbar",
        "crispy_forms",
        "crispy_bootstrap4",
        "allauth",
        "allauth.socialaccount",
        "allauth.socialaccount.providers.github",
        # "myapp.apps.MyappConfig",
    ]
    INTERNAL_IPS = ['127.0.0.1']

    SITE_ID = 1

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

    ROOT_URLCONF = "myproject.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [BASE_DIR / "templates"],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    WSGI_APPLICATION = "myproject.wsgi.application"

    # Database
    # https://docs.djangoproject.com/en/4.0/ref/settings/#databases

    # DATABASES = {
    #     "default": {
    #         "ENGINE": "django.db.backends.sqlite3",
    #         "NAME": BASE_DIR / "db.sqlite3",
    #     }
    # }
    DATABASES = values.DatabaseURLValue(
        f'sqlite:///{BASE_DIR}/db.sqlite3', environ_prefix='DJANGO'
    )
    # Password validation
    # https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/4.0/topics/i18n/

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.0/howto/static-files/

    STATIC_URL = "static/"

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    STATICFILES_DIRS = [BASE_DIR / "static"]

    MEDIA_ROOT = BASE_DIR / "media"
    MEDIA_URL = "/media/"

    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

    CRISPY_TEMPLATE_PACK = "bootstrap4"

class Prod(Dev):
    DEBUG = False
    SECRET_KEY = values.SecretValue()
    # no other settings defined since we're only overriding DEBUG
