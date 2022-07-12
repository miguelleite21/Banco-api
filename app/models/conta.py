from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.models.pessoa import Pessoa

@dataclass
class Conta(db.Model):
    idConta : int
    idPessoa:Pessoa
    saldo : float
    limiteSaqueDiario : float
    flagAtivo : bool
    tipoConta : int
    dataCriacao : str

    __tablename__ = "conta"
    idConta=Column(Integer, primary_key=True)
    saldo = Column(Float, nullable=False)
    limiteSaqueDiario = Column(Float, nullable=False)
    flagAtivo =  Column(Boolean,nullable=False)
    tipoConta = Column(Integer)
    dataCriacao =  Column(Date,nullable=False)
    idPessoa = Column(Integer, ForeignKey("pessoa.idPessoa"),unique=True)

    pessoa = relationship("Pessoa",backref="conta",uselist=False)
  

