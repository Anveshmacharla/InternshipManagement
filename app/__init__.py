from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import User, Internship, Domain  # ✅ Import models only
    from .routes import main  # ✅ Register blueprint after models are loaded

    app.register_blueprint(main)

    return app