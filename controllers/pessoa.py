import json

from flask import Blueprint, request

from models.Pessoa import Pessoa

pessoacontroller = Blueprint("cnpjcontroller",__name__, template_folder="controllers")

@pessoacontroller.route('/api/pessoa/save', methods=["POST"])
def save():
    obj = request.get_json()
    obj_pessoa = Pessoa(obj)
    return Pessoa.toJson(obj_pessoa)