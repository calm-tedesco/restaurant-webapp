from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
        'db': 'restaurant_webapp',
        'username': 'abc',
        'password': 'xyz'
        }
db = MongoEngine(app)

from app import routes
