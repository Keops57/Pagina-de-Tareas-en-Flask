#Estructura basica de Flask

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tareas_pendientes = []
tareas_terminadas = []

# Ruta

#Se coloca un decorador (el @), sirve para indicar que todo lo de abajo del decorador pertenece al mismo, hasta que aparezca otro

@app.route('/')

# Vista (Será la parte de html basicamente)

def index():
    return render_template('index.html', tareas1 = tareas_pendientes, tareas2 = tareas_terminadas)

@app.route('/agregar', methods = ["GET","POST"])

# Las rutas por defecto estan en el metodo GET

def agregar():
#Esto sirve para preguntar: Si en el request(que es todo el url) hay un metodo llamado post, se ejecuta lo de abajo
    if request.method == "POST":
        #Tomamos lo que ingresamos en el form y se iguala a la variable tarea
        nueva_tarea = request.form.get("tarea")
        #Se agrega la tarea a la lista
        tareas_pendientes.append(nueva_tarea)
        #Redirigimos a la pagina principal (la ruta /)
    return redirect('/')

@app.route('/done/<int:id>')

def done(id):
    x = tareas_pendientes.pop(id)
    tareas_terminadas.append(x)
    return redirect('/')

#Las funciones "request" y "redirect" se tienen que importar

if __name__ == "main":
    app.run(debug=True) 