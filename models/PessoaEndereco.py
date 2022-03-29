from utils.pyAtom.repository.PyAtomModel import PyAtomModel

class PessoaEndereco(PyAtomModel):
    def __init__(self, obj):
        self.id = "" if obj.get("id") == None else obj.get("id")
        self.idpessoa = "" if obj.get("idpessoa") == None else obj.get("idpessoa")
        self.logradouro = "" if obj.get("logradouro") == None else obj.get("logradouro")
        self.bairro = "" if obj.get("bairro") == None else obj.get("bairro")
        self.numero = "" if obj.get("numero") == None else obj.get("numero")
        self.complemento = "" if obj.get("complemento") == None else obj.get("complemento")
        self.cep = "" if obj.get("cep") == None else obj.get("cep")


    def __id__(self):
        return "id"

    def __fk__(self):
        return [{"idpessoa": {"pessoa": "id"}}]

    def __alias__(self):
        return [{"dataemissao": "dataemissao"}]

    def __tableName__(self):
        return "pessoa_endereco"
