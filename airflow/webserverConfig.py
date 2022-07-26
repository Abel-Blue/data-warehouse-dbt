
"""Default configuration for the Airflow webserver"""
import os

from flask_appbuilder.security.manager import AUTH_DB


basedir = os.path.abspath(os.path.dirname(__file__))

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True

AUTH_TYPE = AUTH_DB

#Uncomment to setup Full admin role name
AUTH_ROLE_ADMIN = 'Admin'

# Uncomment to setup Public role name, no authentication needed
AUTH_ROLE_PUBLIC = 'Public'

# Will allow user self registration
AUTH_USER_REGISTRATION = True

# The recaptcha it's automatically enabled for user self registration is active and the keys are necessary
RECAPTCHA_PRIVATE_KEY = PRIVATE_KEY
RECAPTCHA_PUBLIC_KEY = PUBLIC_KEY

# Config for Flask-Mail necessary for user self registration
MAIL_SERVER = 'smtp.gmail.com'
MAIL_USE_TLS = True
MAIL_USERNAME = 'yourappemail@gmail.com'
MAIL_PASSWORD = 'passwordformail'
MAIL_DEFAULT_SENDER = 'sender@gmail.com'

# The default user self registration role
AUTH_USER_REGISTRATION_ROLE = "Public"

# When using OAuth Auth, uncomment to setup provider(s) info
# Google OAuth example:
OAUTH_PROVIDERS = [{
  'name':'google',
     'token_key':'access_token',
     'icon':'fa-google',
         'remote_app': {
             'api_base_url':'https://www.googleapis.com/oauth2/v2/',
             'client_kwargs':{
                 'scope': 'email profile'
             },
             'access_token_url':'https://accounts.google.com/o/oauth2/token',
             'authorize_url':'https://accounts.google.com/o/oauth2/auth',
             'request_token_url': None,
             'client_id': GOOGLE_KEY,
             'client_secret': GOOGLE_SECRET_KEY,
         }
 }]
