from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Config)


# MongoEnginer Instantiation
db = MongoEngine()
db.init_app(app)


# Import all the routes
from application import routes
