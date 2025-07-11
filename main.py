from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

app = Flask(__name__)

@app.route('/crear-tarea', methods=['POST'])
def crear():
    tarea = Tarea(contenido=request.form['contenido_tarea'], hecha=False)
    db.session.add(tarea) # Añadimos la tarea a la sesión
    db.session.commit() # Guardamos los cambios en la base de datos
    return redirect(url_for('home'))

@app.route('/eliminar-tarea/<id>')
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).delete()
    db.session.commit() # Ejecutar la operación pendiente de la base de datos
    return redirect(url_for('home'))

@app.route('/tarea-hecha/<id>')
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first() # Se obtiene la tarea que se busca
    tarea.hecha = not(tarea.hecha) # Guardamos en la variable booleana de la tarea, su contrario
    db.session.commit() # Ejecutar la operación pendiente de la base de datos
    return redirect(url_for('home'))
@app.route('/')
def home():
    todas_las_tareas = db.session.query(Tarea).all()  # Obtenemos todas las tareas
    return render_template("index.html", lista_de_tareas=todas_las_tareas)

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)