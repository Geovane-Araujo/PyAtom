from utils.pyAtom.repository.PyAtomModel import PyAtomModel

class Cpf(PyAtomModel):
    def __init__(self, obj):
        self.id = obj.get("id")
        self.cpf = obj.get("cpf")
        self.dataemissao = obj.get("dataemissao")
        self.idpessoa = obj.get("idpessoa")

    def id(self):
        return ["id"]

    def fk(self):
        return [{"idpessoa": {"pessoa": "id"}}]

    def alias(self):
        return [{"dataemissao": "data_emissao"}]

    def tableName(self):
        return "cpf"
