# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.database import db
from flasgger import Swagger

from  models.electro_scooter import ElectroScooter

def create_app():
    app = Flask(__name__)

    # Configure SQLAlchemy to use SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://leonidas:12345@localhost:5432/testpython'
    db.init_app(app)
    Swagger(app)
    return app

if __name__ == "__main__":
    app = create_app()
    import routes
    app.run(host='192.168.111.76', port=5000)