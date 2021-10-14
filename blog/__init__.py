from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os


def create_app():
    app = Flask(__name__)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ee1e2a863e684a583d58ed34c70f7e98'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://rxitjrqxlhcxso:17423ed633133681b51143a0f3b5134944a7ee0b7a71968f4e2e772a8af426ff@ec2-54-155-22-153.eu-west-1.compute.amazonaws.com:5432/d1a6e85j2mqm7l"
db = SQLAlchemy(app)


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from blog import routes

