import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app:Flask):
    app.config['SQLALCHEMY_DATABASE_URI']=os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.db=db
    from app.models import Pessoa,Transacao,Conta
