from flask import Flask, Blueprint
from pymongo import MongoClient
from flask_pymongo import PyMongo
from flask_cors import CORS
import os
from openai import OpenAI
import certifi

openAI_client = OpenAI(
    api_key="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"
)

client = MongoClient(
    "mongodb+srv://yiyanhh:kcyDdQBUnW9Ak6DB@cluster0.hdoctva.mongodb.net/", tlsCAFile=certifi.where())
db = client.get_database("users")
user = db.appname


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.urandom(32)

    # configure CORS to allow requests from frontend
    # allow cookies so that session can be used
    CORS(app, resources={
         r"/api/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
