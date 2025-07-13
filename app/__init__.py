from flask import Flask
# from .extensions import db, migrate

def create_app(config_object=None):
    app = Flask(__name__)

    if config_object:
        app.config.from_object(config_object)

    # db.init_app(app)
    # migrate.init_app(app, db)

    from .routes import bp as my_bp
    app.register_blueprint(my_bp, url_prefix='/api')

    return app
