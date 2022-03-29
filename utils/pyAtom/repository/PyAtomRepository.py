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
            if vars(obj[0])[fieldIdentifier] == '':
                operationPercistence(obj[0],con,0 )
            else:
                operationPercistence(obj[0], con,1)

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


def operationPercistence(obj,con,type):


    if obj.__noEntity__() == True: return

    exec = constructorCommand(obj, type)

    cursor = con.cursor()
    ss = cursor.execute(exec[0],exec[1])
    id = cursor._prep.RETURN_GENERATED_KEYS

    return None

def constructorCommand(obj, type):
    sql = ""
    obj_columns = ""
    values_cor = ""
    values_var = []
    obj_tableName = obj.__tableName__()
    if obj_tableName == "":
        obj_tableName = ""
    if type == 0:

        obj_ignores = []
        #aqui retira os campos que serão ignorados na montagem da sql
        obj_ignores.append(obj.__id__())
        for ig in obj.__ignore__():
            obj_ignores.append(ig)
        for lo in obj.__listObject__():
            obj_ignores.append(lo)
        for so in obj.__simpleObject__():
            obj_ignores.append(so)


        for k in vars(obj):
            if(sum([ct == k for ct in obj_ignores]) == 0):
                obj_columns += k + ","
                values_cor += "?,"
                values_var.append(vars(obj)[k])

        sql = f'INSERT INTO {obj_tableName}({obj_columns[:-1]}) VALUES({values_cor[:-1]})'
    return [sql, values_var]



