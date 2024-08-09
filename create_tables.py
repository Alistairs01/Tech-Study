from run import create_app
from server.extensions import db

app = create_app()

with app.app_context():
    db.create_all()
    print("All tables created successfully.")
