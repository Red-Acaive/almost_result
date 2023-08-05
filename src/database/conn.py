from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import Table, Column, Integer, String


app = Flask(__name__)
app.debug = True

class db_init:
    def __init__(self) -> None:
        self.username = "root"
        self.password = "develop"
        self.dbname = "dev"
    
    def create_db(self):
        app.config['SQLALCHEMY_DATABASE_URI']= f'mysql://{self.username}:{self.password}@mysql:3306/{self.dbname}'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
        db = SQLAlchemy()

        db.init_app(app)

        with app.app_context():
            db.create_all()
    


db_init().create_db()