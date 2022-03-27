from utils.pyAtom.repository.PyAtomModel import PyAtomModel

class PessoaTelefone(PyAtomModel):
    def __init__(self, obj):
        self.id = obj["id"]
        self.idpessoa = obj["idpessoa"]
        self.telefone = obj["telefone"]

    def __id__(self):
        return ["id"]

    def __fk__(self):
        return [{"idpessoa": {"pessoa": "id"}}]

    def __tableName__(self):
        return "pessoa_telefone"
