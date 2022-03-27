from flask import Flask
from controllers.pessoa import pessoacontroller

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Não Autorizado!'

app.register_blueprint(pessoacontroller)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
