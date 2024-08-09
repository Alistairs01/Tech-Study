from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load configuration from server.config.Config
    app.config.from_object('server.config.Config')

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    # Register blueprints or import routes
    with app.app_context():
        from server import routes
        from server import models
    
    return app
