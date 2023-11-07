from flask import Flask, render_template
# captuando todo flask 
app = Flask(__name__)
# ruta raiz
@app.route('/')
def inicio():
  titulo = "Bienvenido"
  return render_template('inicio.html', titulo=titulo)

# ruta equipo
@app.route('/equipo')
def equipo():
    titulo = "Equipo Liceo Industrial"
    return render_template('equipo.html', titulo=titulo)
  


# bloque de prueba para flask 
if __name__ == "__main__":
  app.run(debug=True)
