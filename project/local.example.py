# Overrides
from .settings import *  # noqa: F401

SECRET_KEY = 'lksdf98wrhkjs88dsf8-324ksdm'

DEBUG = True

# for setup using postgres:
# start the psql interactive prompt and create a user (e.g. "Barney") with a password (e.g. "dinosaurking#1") with createdb role attributes
# exit the interactive prompt
# start the prompt with the new user ("Barney")
# create database (e.g. "gtd")
# exit the interactive prompt
# copy the contents of this file into a "local.py" file in the same directory as this file
# run "python manage.py migrate"
# run "python manage.py makemigrations"
# run "python manage.py runserver"
# make user "local.py is in your .gitignore"
# violà

# access the admin dashboard via http://127.0.0.1:8000/gtdadmin/ if using localhost and local.py for settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gtd',
        'USER': 'Barney',
        'PASSWORD': 'dinosaurking#1',
        'HOST': '127.0.0.1',
        'PORT': '',
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# TODO-specific settings
TODO_STAFF_ONLY = False
TODO_DEFAULT_LIST_SLUG = 'tickets'
TODO_DEFAULT_ASSIGNEE = None
TODO_PUBLIC_SUBMIT_REDIRECT = '/'