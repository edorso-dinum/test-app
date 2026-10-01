"""
Django settings for the test-app project.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY", "django-insecure-test-app-secret-key"
)

DEBUG = os.environ.get("DJANGO_DEBUG", "true").lower() == "true"

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "*").split(",")

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "roles",
    "doublures",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Each table lives in its own PostgreSQL database, hosted by the CNPG cluster
# and seeded by the scripts in `data/` as a migration step:
# - `data/premier_roles.sql` fills the `premier_roles` database's `role_names` table.
# - `data/doublure.sql` fills the `doublures` database's `doublure_names` table.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "premier_roles": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("PREMIER_ROLES_DB_NAME", "premier_roles"),
        "USER": os.environ.get("PREMIER_ROLES_DB_USER", "postgres"),
        "PASSWORD": os.environ.get("PREMIER_ROLES_DB_PASSWORD", ""),
        "HOST": os.environ.get("PREMIER_ROLES_DB_HOST", "localhost"),
        "PORT": os.environ.get("PREMIER_ROLES_DB_PORT", "5432"),
    },
    "doublures": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DOUBLURES_DB_NAME", "doublures"),
        "USER": os.environ.get("DOUBLURES_DB_USER", "postgres"),
        "PASSWORD": os.environ.get("DOUBLURES_DB_PASSWORD", ""),
        "HOST": os.environ.get("DOUBLURES_DB_HOST", "localhost"),
        "PORT": os.environ.get("DOUBLURES_DB_PORT", "5432"),
    },
}

DATABASE_ROUTERS = ["config.routers.DatabaseRouter"]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
