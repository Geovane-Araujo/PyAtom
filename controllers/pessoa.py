import json

from flask import Blueprint, request

from handlers.PessoaImpl import PessoaImpl
from models.Pessoa import Pessoa

pessoacontroller = Blueprint("cnpjcontroller",__name__, template_folder="controllers")

@pessoacontroller.route('/api/pessoa/save', methods=["POST"])
def save():
    obj = request.get_json()
    obj_pessoa = Pessoa(obj)
    ret = PessoaImpl.save(obj_pessoa)
    return Pessoa.toJson(obj_pessoa)