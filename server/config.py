#server/config.py

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:database@localhost:5432/techstudy"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "development key"
    