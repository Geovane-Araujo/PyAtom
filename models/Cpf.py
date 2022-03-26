from utils.pyAtom.repository.PyAtomModel import PyAtomModel

class Cpf(PyAtomModel):
    def __init__(self, obj):
        self.id = obj.get("id")
        self.cpf = obj.get("cpf")
        self.dataemissao = obj.get("dataemissao")
        self.idpessoa = obj.get("idpessoa")

    def __id__(self):
        return ["id"]

    def __fk__(self):
        return [{"idpessoa": {"pessoa": "id"}}]

    def __alias__(self):
        return [{"dataemissao": "data_emissao"}]

    def __tableName__(self):
        return "cpf"
