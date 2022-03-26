from utils.pyAtom.repository.PyAtomModel import PyAtomModel

class Cpf(PyAtomModel):
    def __init__(self, obj):
        self.id = obj.get("id")
        self.idpessoa = obj.get("idpessoa")
        self.logradouro = obj.get("logradouro")
        self.bairro = obj.get("bairro")
        self.numero = obj.get("numero")
        self.complemento = obj.get("complemento")
        self.cep = obj.get("cep")


    def id(self):
        return ["id"]

    def fk(self):
        return [{"idpessoa": {"pessoa": "id"}}]

    def alias(self):
        return [{"dataemissao": "dataemissao"}]

    def tableName(self):
        return "pessoa_endereco"
