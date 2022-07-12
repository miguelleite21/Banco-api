from flask import jsonify, request
from app.models.conta import Conta
from app.models.pessoa import Pessoa
from app.models.transacao import Transacao
from app.configs.database import db
import psycopg2
import sqlalchemy
from datetime import datetime

date = datetime.now()
def post_conta():
    data = request.get_json()
    
    try:
        
        pessoa = Pessoa.query.filter_by(cpf=data.pop("cpf")).first()
        if not pessoa:
            return {"error": "pessoa not found"}, 404
            
        data['saldo'] = 0.00
        data['flagAtivo'] = True
        data['limiteSaqueDiario'] = 1000.00
        data['tipoConta'] = 1
        data['dataCriacao'] = date
        conta = Conta(**data)
        print("teste",pessoa)
        conta.idPessoa = pessoa.idPessoa
       

    except TypeError:
        return {"Error": "valid kays is [cpf]"}, 400

    try:
        db.session.add(conta)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError as e:

        if isinstance(e.orig, psycopg2.errors.UniqueViolation):
            return {"error": "Unique Violation"}, 400

        return {"error": "Integrity Error"}, 400
    print(conta)
    return jsonify(conta), 200


def get_conta(idConta:int):

    conta = Conta.query.get(idConta)
    if not conta:
        return {"error": "id not found"}, 404
    if not conta.flagAtivo: 
        return {"error": "blocked account "}, 400

    return jsonify(conta.saldo), 200

def add_saldo(idConta:int):
    try:
        conta = Conta.query.get(idConta)
        data = request.get_json()
        if not conta:
            return {"error": "id not found"}, 404
        if not conta.flagAtivo: 
            return {"error": "blocked account "}, 400

        setattr(conta,"saldo",data['saldo']+conta.saldo)

        transacaoData = {
            "idConta":conta.idConta,
            "valor":data['saldo'],
            "dataTransacao":date
        }

        transacao = Transacao(**transacaoData)
        db.session.add(transacao)
        db.session.commit()
        return jsonify(conta.saldo),200
    except KeyError:
        return {"Error": "valid kays is [saldo]"}, 400

def down_saldo(idConta:int):
    try:
        conta = Conta.query.get(idConta)
        data = request.get_json()
        if not conta:
            return {"error": "id not found"}, 404
        if not conta.flagAtivo: 
            return {"error": "blocked account "}, 400
        if conta.limiteSaqueDiario < data['saque']:
            return {"error": "your daily withdrawal limit is: "+ str( conta.limiteSaqueDiario)}, 400
        if conta.saldo < data['saque']:
            return {"error": "insufficient funds"}, 400

        setattr(conta,"saldo",conta.saldo-data['saque'])

        transacaoData = {
            "idConta":conta.idConta,
            "valor":0-data['saque'],
            "dataTransacao":date
        }
        transacao = Transacao(**transacaoData)
        db.session.add(transacao)
        db.session.commit()
        return jsonify(conta.saldo),200
    except KeyError:
        return {"Error": "valid kays is [saque]"}, 400

def block_conta(idConta:int):   
        conta = Conta.query.get(idConta)
        if not conta:
            return {"error": "id not found"}, 404
        if not conta.flagAtivo: 
            return {"error": "blocked account "}, 400
        setattr(conta,"flagAtivo",False)
        db.session.commit()
        return jsonify(conta),200

def get_transacao(idConta:int):

    conta = Conta.query.get(idConta)
    if not conta:
            return {"error": "id not found"}, 404
    

    return jsonify(conta.transacao), 200