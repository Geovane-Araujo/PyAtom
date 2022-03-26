from utils.pyAtom.repository.PyAtomModel import PyAtomModel

class Cpf(PyAtomModel):
    def __init__(self, obj):
        self.id = obj.get("id")
        self.rg = obj.get("rg")
        self.dataemissao = obj.get("dataemissao")
        self.idpessoa = obj.get("idpessoa")

    def id(self):
        return ["id"]

    def fk(self):
        return [{"idpessoa": {"pessoa": "id"}}]

    def alias(self):
        return [{"dataemissao": "dataemissao"}]

    def tableName(self):
        return "rg"
