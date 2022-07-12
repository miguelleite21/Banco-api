from flask import Blueprint, Flask
from app.routes.pessoa_route import bp_pessoa
from app.routes.conta_route import bp_conta
bp_api = Blueprint("api",__name__)

def init_app(app:Flask):
    bp_api.register_blueprint(bp_pessoa)
    bp_api.register_blueprint(bp_conta)

    app.register_blueprint(bp_api)