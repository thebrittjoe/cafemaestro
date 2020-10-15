from flask import Flask
from config import Config
from app.models import User, Role, db
from flask_security import Security, SQLAlchemyUserDatastore
from flask_migrate import Migrate

#looks for changes to column types
migrate = Migrate(compare_type=True)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app)
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    # register our blueprints here
    from app.manager import bp as manager_manager
    app.register_blueprint(manager_manager, url_prefix='/mgmt')

    from app.public import bp as public_public
    app.register_blueprint(public_public)

    return app