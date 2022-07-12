from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy.orm  import relationship
from sqlalchemy import  Column, Date, Float, ForeignKey, Integer, String

@dataclass
class Transacao(db.Model):

    idTransacao:int
    idConta:int
    valor:float
    dataTransacao:str

    __tablename__ = "transacao"
    idTransacao=Column(Integer, primary_key=True)
    valor = Column(Float, nullable=False)
    dataTransacao =  Column(Date,nullable=False)
    idConta = Column(Integer,ForeignKey("conta.idConta"),nullable=False)


    conta = relationship("Conta",backref="transacao")