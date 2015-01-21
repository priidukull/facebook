import os

from flask import Flask
from flask.ext.login import LoginManager

from parameters import action_var


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_object('config')
print('MODE=%s' % os.environ.get('MODE'))
if action_var == 'bo':
    from app import views, models