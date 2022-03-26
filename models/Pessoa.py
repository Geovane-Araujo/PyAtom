from models.Cpf import Cpf
from models.PessoaEndereco import PessoaEndereco
from models.PessoaTelefone import PessoaTelefone
from models.Rg import Rg
from utils.pyAtom.repository.PyAtomModel import PyAtomModel

class Pessoa(PyAtomModel):
    def __init__(self, obj):
        self.id = obj.get("id")
        self.nome = obj.get("nome")
        self.idade = obj.get("idade")
        self.idTipoPessoa = obj.get("idTipoPessoa")
        self.pessoaTelefone = PessoaTelefone(obj.get("pessoaTelefone"))
        self.pessoaEndereco = PessoaEndereco(obj.get("pessoaEndereco"))
        self.cpf = Cpf(obj.get("cpf"))
        self.rg = Rg(obj.get("rg"))
        self.descricaoTipo = obj.get("descricaoTipo")

    def __id__(self):
        return ["id"]

    def __tableName__(self):
        return "pessoa"

    def __listObject__(self):
        return ["pessoaTelefone"]

    def __simpleObject__(self):
        return ["pessoaEndereco", "rg", "cpf"]

    def __ignore__(self):
        return ["descricaoTipo"]