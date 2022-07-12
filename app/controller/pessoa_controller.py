from flask import jsonify, request
from app.models.pessoa import Pessoa
from app.configs.database import db
from app.exc import InvalidCpfError,InvalidDateFormatError
import psycopg2
import sqlalchemy

def post_pessoa():
    data = request.get_json()

    try:
        pessoa = Pessoa(**data)
    except InvalidCpfError:
        return {"Error": "Invalid CPF"},400
    except InvalidDateFormatError:
        return {"Error": "date format must be `yyyy/mm/dd`"}, 400
    except TypeError:
        return {"Error": "valid kays is [nome,cpf,dataNascimento]"}, 400

    try:
        db.session.add(pessoa)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError as e:

        if isinstance(e.orig, psycopg2.errors.UniqueViolation):
            return {"error": "Unique Violation"}, 400

        return {"error": "Integrity Error"}, 400
    return jsonify(pessoa), 200
    

