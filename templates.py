# Imports de librerias 
from flask import Flask
from flask import render_template

# Declaracion del app
app = Flask(__name__)


# Rutas
@app.route("/<name>")
def index(name):
    return render_template('index.html', nombre=name, age=18, items = ["item1", "item2", "item3"])
    

# Servidor en 0.0.0.0 y 8080

if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")