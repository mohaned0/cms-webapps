"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from flask.logging import create_logger

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
logging.basicConfig(
    
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
