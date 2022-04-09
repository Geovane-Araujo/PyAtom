from flask import Flask
from controllers.pessoa import pessoacontroller
from utils.pyAtom.models.GlobalVariables import ConfigPyAtom

app = Flask(__name__)

ConfigPyAtom.path_properties = app.root_path + "/atom_config.json"
ConfigPyAtom.path_jdbc = app.root_path + "/libsconn/mssql.jar"

@app.route('/')
def hello_world():
    return 'Não Autorizado!'

app.register_blueprint(pessoacontroller)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
