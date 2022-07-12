from flask import Blueprint
from app.controller.pessoa_controller import post_pessoa

bp_pessoa = Blueprint("pessoas",__name__, url_prefix="/pessoa")

bp_pessoa.post("")(post_pessoa)
