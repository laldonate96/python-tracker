from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = MongoClient(os.environ.get("DATABASE_URL"))
app.db = client.get_default_database()

app.register_blueprint(pages)