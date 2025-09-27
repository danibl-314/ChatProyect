from flask import Flask, render_template, request, redirect, url_for
import database as db  # Asegúrate de que tu archivo de funciones de DB se llame 'database.py'
import sqlite3 # Necesario para manejar errores específicos

app = Flask(__name__)

# --- RUTAS ESTÁTICAS Y DE NAVEGACIÓN (GET) ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vision')
def vision():
    return render_template('vision.html')

@app.route('/mision')
def mision():
    return render_template('mision.html')

# --- RUTAS DEL CHATBOX ---

@app.route('/chat')
def chat():
    """Muestra el formulario de la interfaz del chatbot."""
    return render_template('chat.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Maneja el envío del formulario, procesa el mensaje del usuario y devuelve una respuesta."""
    if request.method == 'POST':
        user_prompt = request.form['prompt']
        
        # --- Lógica de Gemini (Placeholder) ---
        if "universidad" in user_prompt.lower():
            model_response = "¡Hola! ¿Estás interesado en nuestros programas de Ingeniería de Sistemas?"
        else:
            model_response = f"Recibí tu mensaje: '{user_prompt}'. Procesando tu solicitud..."
        # --------------------------------------
        
        return render_template(
            'chat.html', 
            user_prompt=user_prompt, 
            model_response=model_response
        )
        
    return redirect(url_for('chat'))

# --- RUTA DE PROGRAMAS (CRUD - READ) ---

@app.route('/programas')
def programas():
    conn = db.create_connection()
    carreras = []
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM carrera")
            carreras = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error consultando la base de datos: {e}")
        finally:
            conn.close()
    
    return render_template('programas.html', carreras=carreras)

# --- RUTA PARA AGREGAR PROGRAMAS (CRUD - CREATE) ---

@app.route('/agregar_programa', methods=['POST'])
def agregar_programa():
    if request.method == 'POST':
        descripcion = request.form['descripcion_carrera']
        conn = db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO carrera (descripcion) VALUES (?)", (descripcion,))
                conn.commit()
            except sqlite3.IntegrityError:
                conn.close()
                return "Error: Este programa ya existe. <a href='/programas'>Volver</a>", 409
            except sqlite3.Error as e:
                print(f"Error al agregar programa: {e}")
                conn.close()
                return "Error al agregar el programa.", 500
            finally:
                if conn:
                    conn.close()

    return redirect(url_for('programas')) 

# --- RUTA DE EDICIÓN (CRUD - UPDATE) ---

@app.route('/editar/<int:id>', methods=('GET', 'POST'))
def editar_carrera(id):
    carrera = db.get_carrera(id) 
    
    if request.method == 'POST':
        new_descripcion = request.form['descripcion_carrera']
        
        if db.update_carrera(id, new_descripcion):
            return redirect(url_for('programas'))
        else:
            return "Error al actualizar la carrera", 500

    if carrera:
        return render_template('editar_carrera.html', carrera=carrera)
    else:
        return "Carrera no encontrada", 404

# --- RUTA DE ELIMINACIÓN (CRUD - DELETE) ---

@app.route('/eliminar/<int:id>', methods=('POST',))
def eliminar_carrera(id):
    if db.delete_carrera(id):
        return redirect(url_for('programas'))
    else:
        return "Error al eliminar la carrera", 500

# --- INICIO DEL SERVIDOR ---

if __name__ == '__main__':
    # Inicializa la base de datos (solo la primera vez que se ejecuta)
    db.init_db()
    
    # Inicia el servidor Flask
    app.run(debug=True)