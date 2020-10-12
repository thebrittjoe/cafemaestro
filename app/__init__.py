from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    # register our blueprints here
    from app.manager import bp as manager_manager
    app.register_blueprint(manager_manager, url_prefix='/mgmt')

    from app.public import bp as public_public
    app.register_blueprint(public_public)

    return app