import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from models import db
from dotenv import load_dotenv
from routes import api

load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

db.init_app(app)
Migrate(app, db)
CORS(app)

app.register_blueprint(api, url_prefix="/api")

app.route('/')
def main():
    return jsonify({ "msg": "API REST FLASK"})


if __name__ == '__main__':
    app.run()