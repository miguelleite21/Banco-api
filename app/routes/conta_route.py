from audioop import add
from flask import Blueprint
from app.controller.conta_controller import post_conta,get_conta,add_saldo,down_saldo,block_conta,get_transacao

bp_conta = Blueprint("contas",__name__, url_prefix="/conta")

bp_conta.post("")(post_conta)
bp_conta.get("saldo/<int:idConta>")(get_conta)
bp_conta.get("transacao/<int:idConta>")(get_transacao)
bp_conta.patch("/saldo/<int:idConta>")(add_saldo)
bp_conta.patch("/saque/<int:idConta>")(down_saldo)
bp_conta.patch("/bloqueio/<int:idConta>")(block_conta)