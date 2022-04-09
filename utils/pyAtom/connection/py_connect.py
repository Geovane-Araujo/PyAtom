import json

import jaydebeapi


from utils.pyAtom.models.GlobalVariables import ConfigPyAtom



def connect_db(*args):
    config = config_read(ConfigPyAtom.path_properties)
    if len(args) > 0:
        config['connection_db']['db_name'] = args[0]

    if(config.get("connection_db").get("schema") != None):
        ConfigPyAtom.schema = True
        ConfigPyAtom.schema_name = config.get("connection_db").get("schema")

    if config.get("connection_db").get("db") == "MYSQL":
        return py_mysql_connect(config.get("connection_db"))
    elif config.get("connection_db").get("db") == "POSTGRES":
        return py_pg_connect(config.get("connection_db"))
    elif config.get("connection_db").get("db") == "MSSQL":
        return py_mssql_connect(config.get("connection_db"))

def py_pg_connect(config):
    con = jaydebeapi.connect(
        "org.postgresql.Driver",
        f"jdbc:postgresql://{config.get('url')}:{config.get('port')}/{config.get('db_name')}",
        [config.get("user"), config.get("password")],
        ConfigPyAtom.path_jdbc
    )
    con.jconn.setAutoCommit(False)
    return con

def py_mssql_connect(config):
    con = jaydebeapi.connect(
        "com.microsoft.sqlserver.jdbc.SQLServerDriver",
        f"jdbc:sqlserver://{config.get('url')}:{config.get('port')};database={config.get('db_name')};trustServerCertificate=true;encrypt=true;",
        [config.get("user"),config.get("password")],
        ConfigPyAtom.path_jdbc
    )
    con.jconn.setAutoCommit(False)
    return con

def py_mysql_connect(config):
    con = jaydebeapi.connect(
        "com.mysql.jdbc.Driver",
        f"jdbc:mysql://{config.get('url')}:{config.get('port')}/{config.get('db_name')}",
        [config.get("user"), config.get("password")],
        ConfigPyAtom.path_jdbc
    )
    con.jconn.setAutoCommit(False)
    return con

def config_read(config):

    with open(config, 'r', encoding='utf8') as f:
        return json.load(f)


