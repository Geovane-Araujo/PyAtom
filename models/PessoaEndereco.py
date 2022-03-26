from utils.pyAtom.repository.PyAtomModel import PyAtomModel

class PessoaEndereco(PyAtomModel):
    def __init__(self, obj):
        self.id = obj.get("id")
        self.idpessoa = obj.get("idpessoa")
        self.logradouro = obj.get("logradouro")
        self.bairro = obj.get("bairro")
        self.numero = obj.get("numero")
        self.complemento = obj.get("complemento")
        self.cep = obj.get("cep")


    def __id__(self):
        return ["id"]

    def __fk__(self):
        return [{"idpessoa": {"pessoa": "id"}}]

    def __alias__(self):
        return [{"dataemissao": "dataemissao"}]

    def __tableName__(self):
        return "pessoa_endereco"
