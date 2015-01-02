from flask import Flask
from flask.ext.login import LoginManager, logout_user


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_object('config')
from app import views, models