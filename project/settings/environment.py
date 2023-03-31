import os
from pathlib import Path

from utils.environment import get_env_variable, parse_comma_sep_str_to_list

if os.environ.get("DEBUG", None) is None:
    from dotenv import load_dotenv
    load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'INSECURE')  # noqa: E501,

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.environ.get("DEBUG") == "1" else False

# APPEND_SLASH = False
# PREPEND_WWW = False

# Está permitindo qualquer site de usar nossa aplicação django e não é seguro
ALLOWED_HOSTS: list[str] = parse_comma_sep_str_to_list(
    get_env_variable('ALLOWED_HOSTS')
)
CSRF_TRUSTED_ORIGINS: list[str] = parse_comma_sep_str_to_list(
    get_env_variable('CSRF_TRUSTED_ORIGINS')
)

ROOT_URLCONF = "project.urls"

WSGI_APPLICATION = "project.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"