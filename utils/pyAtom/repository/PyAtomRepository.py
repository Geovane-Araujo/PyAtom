from abc import ABC
from utils.pyAtom.connection.py_connect import connect_db

class PyAtomRepository(ABC):

    #persiste no db
    @classmethod
    def save(self, *obj):
        fieldIdentifier = obj[0].__id__()
        con = None
        try:
            if len(obj) > 1:
                con = connect_db(obj[1])
            else:
                con = connect_db()
            if vars(obj[0])[fieldIdentifier] == '':
                operationPercistence(obj[0],con,0 )
            else:
                operationPercistence(obj[0], con,1)

            con.commit()
            return obj[0]
        except Exception as er:
            con.rollback()
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

    id = ""
    no_entity =  obj.__noEntity__()


    if not no_entity:
        exec = constructorCommand(obj, type)
        cursor = con.cursor()
        cursor.execute(exec[0],exec[1])
        cursor.execute(f"select max({obj.__id__()}) FROM {exec[2]}")
        id = cursor.fetchone()[0]
        vars(obj)[obj.__id__()] = id
        cursor.close()
    else:
        id = vars(obj)[obj.__id__()]
        no_entity = True
    recurse = True

    column_id = ""
    while(recurse):

        fields = vars(obj)

        for field in fields:

            if field in obj.__simpleObject__():
                if not no_entity:
                    column_id = fields[field].__id__()
                else:
                    column_id = list(obj.__fk__()[0][field].keys())[0]

                fk = list(fields[field].__fk__()[0])[0]
                vars(fields[field])[fk] = id

                operationPercistence(fields[field],con,type)
            elif field in obj.__listObject__():

                for lifield in vars(obj)[field]:

                    li_fields = vars(lifield)
                    if not no_entity:
                        column_id = lifield.__id__()
                    else:
                        column_id = list(lifield.__fk__()[0].keys())[0]

                    fk = list(lifield.__fk__()[0])[0]
                    li_fields[fk] = id
                    operationPercistence(lifield, con, type)

        recurse = False

    return obj

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
        return [sql, values_var,obj_tableName]

    else:
        obj_ignores = []
        value_id = 0
        # aqui retira os campos que serão ignorados na montagem da sql
        obj_ignores.append(obj.__id__())
        for ig in obj.__ignore__():
            obj_ignores.append(ig)
        for lo in obj.__listObject__():
            obj_ignores.append(lo)
        for so in obj.__simpleObject__():
            obj_ignores.append(so)

        for k in vars(obj):
            if (sum([ct == k for ct in obj_ignores]) == 0):
                obj_columns += k + " = ?,"
                values_var.append(vars(obj)[k])
            elif k == obj.__id__():
                value_id = vars(obj)[k]

        values_var.append(value_id)
        sql = f'UPDATE {obj_tableName} SET {obj_columns[:-1]} WHERE {obj.__id__()} = ?)'
        return [sql, values_var, obj_tableName]



