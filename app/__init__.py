from flask import Flask

app = Flask(__name__)

from app import routes          # must import the module here because 'app' is partially initialized
