from abc import ABC
from utils.pyAtom.connection.py_connect import connect_db

class PyAtomRepository(ABC):

    #persiste no db
    @classmethod
    def save(self, *obj):
        con = None
        column_id = ""

        fieldIdentifier = obj[0].__id__()

        try:
            con = connect_db()
            print("ond")
        except Exception as er:
            ret = {
                "error": er
            }
            return ret

    #methods get
    @classmethod
    def get(self):
        pass

    @classmethod
    def getById(self, obj):
        pass

    @classmethod
    def getAll(self):
        pass

    #execute queryes
    @classmethod
    def execute(self):
        pass

    @classmethod
    def execute(self):
        pass


