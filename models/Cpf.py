from utils.pyAtom.repository.PyAtomModel import PyAtomModel

class Cpf(PyAtomModel):
    def __init__(self, obj):
        self.id = "" if obj.get("id") == None else obj.get("id")
        self.cpf = "" if obj.get("cpf") == None else obj.get("cpf")
        self.dataemissao = "" if obj.get("dataemissao") == None else obj.get("dataemissao")
        self.idpessoa = "" if obj.get("idpessoa") == None else obj.get("idpessoa")

    def __id__(self):
        return "id"

    def __fk__(self):
        return [{"idpessoa": {"pessoa": "id"}}]

    def __alias__(self):
        return [{"dataemissao": "data_emissao"}]

    def __tableName__(self):
        return "cpf"
