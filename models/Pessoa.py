from models.Cpf import Cpf
from models.PessoaEndereco import PessoaEndereco
from models.PessoaTelefone import PessoaTelefone
from models.Rg import Rg
from utils.pyAtom.repository.PyAtomModel import PyAtomModel

class Pessoa(PyAtomModel):
    def __init__(self, obj):
        self.id = obj["id"]
        self.nome = obj["nome"]
        self.idade = obj["idade"]
        self.idTipoPessoa = obj["idTipoPessoa"]
        self.pessoaTelefone = PessoaTelefone(obj["pessoaTelefone"])
        self.pessoaEndereco = PessoaEndereco(obj["pessoaEndereco"])
        self.cpf = Cpf(obj["cpf"])
        self.rg = Rg(obj["rg"])
        self.descricaoTipo = obj["descricaoTipo"]

    def __id__(self):
        return ["id"]

    def __fk__(self):
        return [{"idTipoPessoa": {"pessoa_tipo": "id"}}]

    def __tableName__(self):
        return "pessoa"

    def __listObject__(self):
        return ["pessoaTelefone"]

    def __simpleObject__(self):
        return ["pessoaEndereco", "rg", "cpf"]

    def __ignore__(self):
        return ["descricaoTipo"]

    def __join__(self):
        return [{"descricaoTipo": "descricao"}]

    def __alias__(self):
        pass

    def __noEntity__(self):
        pass

    def __union__(self):
        pass

