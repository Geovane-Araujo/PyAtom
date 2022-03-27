from utils.pyAtom.repository.PyAtomModel import PyAtomModel

class PessoaTelefone(PyAtomModel):
    def __init__(self, obj):
        self.id = "" if obj.get("id") == None else obj.get("id")
        self.idpessoa = "" if obj.get("idpessoa") == None else obj.get("idpessoa")
        self.telefone = "" if obj.get("telefone") == None else obj.get("telefone")


    def __id__(self):
        return ["id"]

    def __fk__(self):
        return [{"idpessoa": {"pessoa": "id"}}]

    def __tableName__(self):
        return "pessoa_telefone"
