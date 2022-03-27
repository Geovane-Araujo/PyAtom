from models.Cpf import Cpf
from models.PessoaEndereco import PessoaEndereco
from models.PessoaTelefone import PessoaTelefone
from models.Rg import Rg
from utils.pyAtom.repository.PyAtomModel import PyAtomModel

class Pessoa(PyAtomModel):
    def __init__(self, obj):
        self.id = "" if obj.get("id") == None else obj.get("id")
        self.nome = "" if obj.get("nome") == None else obj.get("nome")
        self.idade = "" if obj.get("idade") == None else obj.get("idade")
        self.idTipoPessoa = "" if obj.get("idTipoPessoa") == None else obj.get("idTipoPessoa")
        self.pessoaTelefone = [] if obj.get("pessoaTelefone") == None else PessoaTelefone.toArray(obj.get("pessoaTelefone"))
        self.pessoaEndereco = "" if obj.get("pessoaEndereco") == None else PessoaEndereco(obj.get("pessoaEndereco"))
        self.cpf = "" if obj.get("cpf") == None else Cpf(obj.get("cpf"))
        self.rg = "" if obj.get("rg") == None else Rg(obj.get("rg"))
        self.descricaoTipo = "" if obj.get("descricaoTipo") == None else obj.get("descricaoTipo")

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


