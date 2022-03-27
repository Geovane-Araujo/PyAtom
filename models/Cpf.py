from utils.pyAtom.repository.PyAtomModel import PyAtomModel

class Cpf(PyAtomModel):
    def __init__(self, obj):
        self.id = obj["id"]
        self.cpf = obj["cpf"]
        self.dataemissao = obj["dataemissao"]
        self.idpessoa = obj["idpessoa"]

    def __id__(self):
        return ["id"]

    def __fk__(self):
        return [{"idpessoa": {"pessoa": "id"}}]

    def __alias__(self):
        return [{"dataemissao": "data_emissao"}]

    def __tableName__(self):
        return "cpf"
