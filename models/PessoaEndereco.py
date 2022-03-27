from utils.pyAtom.repository.PyAtomModel import PyAtomModel

class PessoaEndereco(PyAtomModel):
    def __init__(self, obj):
        self.id = obj["id"]
        self.idpessoa = obj["idpessoa"]
        self.logradouro = obj["logradouro"]
        self.bairro = obj["bairro"]
        self.numero = obj["numero"]
        self.complemento = obj["complemento"]
        self.cep = obj["cep"]


    def __id__(self):
        return ["id"]

    def __fk__(self):
        return [{"idpessoa": {"pessoa": "id"}}]

    def __alias__(self):
        return [{"dataemissao": "dataemissao"}]

    def __tableName__(self):
        return "pessoa_endereco"
