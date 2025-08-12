from flask import Flask
from flask_cors import CORS
from .routes.auth import auth_bp
from .routes.get_data import get_data_bp
import secrets
import os
from .models import db
from flask_sqlalchemy import SQLAlchemy
import dotenv
# from .extensions import db, migrate

def create_app(config_object=None):
    app = Flask(__name__)
    app.secret_key = secrets.token_hex(16) # csak tesztelésre
    CORS(app, origins=['http://localhost:4200'])

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(get_data_bp, url_prefix='/get-data')

    # from .routes import bp as my_bp
    # app.register_blueprint(my_bp, url_prefix='/api')

    return app
