from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('main/settings.py')
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    from myapp.main.routes import main
    app.register_blueprint(main)


    return app
