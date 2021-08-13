from flask import Flask
from flask_pymongo import PyMongo
from flask_wtf.csrf import CSRFProtect
import config

csrf = CSRFProtect()

app = Flask(__name__)
app.config.from_object(config)
csrf.init_app(app)

db_client = PyMongo(app, uri=f"{config.MONGO_URI}/{config.MONGODB_DATABASE}")
db = db_client.db

from app import urls
