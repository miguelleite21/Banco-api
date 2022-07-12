from app.configs.database import db
from sqlalchemy import Column, Date, Integer, String
from datetime import datetime
from dataclasses import dataclass
from app.exc import InvalidCpfError,InvalidDateFormatError
from sqlalchemy.orm import validates

@dataclass
class Pessoa(db.Model):
    idPessoa: int
    nome:str
    cpf:str
    dataNascimento:str

    __tablename__ = "pessoa"
    idPessoa=Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False, unique=True)
    dataNascimento =  Column(Date,nullable=False)


    @validates("cpf")
    def validate_cpf(self, key, cpf_to_be_tested):
        if len(cpf_to_be_tested) != 11:
            raise InvalidCpfError

        return cpf_to_be_tested
    @validates("dataNascimento")
    def validate_dataNascimento(self, key, date_to_be_tested):
        try:
            b_date = datetime.strptime(date_to_be_tested, "%Y/%m/%d")
        except ValueError:
            raise InvalidDateFormatError
        

        return date_to_be_tested
        