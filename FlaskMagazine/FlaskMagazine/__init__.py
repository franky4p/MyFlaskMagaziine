
from flask import Flask
import FlaskMagazine.config as config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
import FlaskMagazine.views
