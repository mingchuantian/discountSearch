from flask import Flask
from config import Config
import csv
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

from app import routes, forms, main, crawler, write_csv