from utils.pyAtom.repository.PyAtomModel import PyAtomModel

class Rg(PyAtomModel):
    def __init__(self, obj):
        self.id = "" if obj.get("id") == None else obj.get("id")
        self.rg = "" if obj.get("rg") == None else obj.get("rg")
        self.dataemissao = "" if obj.get("dataemissao") == None else obj.get("dataemissao")
        self.idpessoa = "" if obj.get("idpessoa") == None else obj.get("idpessoa")

    def __id__(self):
        return ["id"]

    def __fk__(self):
        return [{"idpessoa": {"pessoa": "id"}}]

    def __alias__(self):
        return [{"dataemissao": "dataemissao"}]

    def __tableName__(self):
        return "rg"
