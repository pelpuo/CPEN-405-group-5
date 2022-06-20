from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy
from keras.models import load_model

def create_database(app):
    if not path.exists("main/"+ DB_NAME):
        db.create_all(app=app)
        print('Created db')


model = load_model('stock_prediction_model.h5')

db = SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from .views import views
from .handlers import handlers

app.register_blueprint(views, url_prefix="/")
app.register_blueprint(handlers, url_prefix="/")