# Imports de librerias 
from flask import Flask
from flask import request

# Declaracion del app
app = Flask(__name__)


# Rutas
@app.route("/")
def index():
    return 'Hola Mundo'
    
    
@app.route("/params")
@app.route("/params/<name>/")
@app.route("/params/<name>/<int:num>")
def params(num, name = "nil"):
    param = request.args.get('params1', 'No contiene este parametro')
    return 'El parametro es {} y {}'.format(name, num)

# Servidor en 0.0.0.0 y 8080

if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")
