from flask import Flask
from blueprint import bp


app = Flask(__name__)
app.register_blueprint(bp)
