
from flask import Flask, render_template, request
import database as db  # Import the new database module
import sqlite3
app = Flask(__name__)

# Route to display the programs
@app.route('/programas')
def programas():
    conn = db.create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # Select all existing programs from the database
            cursor.execute("SELECT * FROM carrera")
            carreras = cursor.fetchall()  # This gets all rows as a list of dictionaries
        except sqlite3.Error as e:
            print(f"Error querying database: {e}")
            carreras = []
        finally:
            conn.close()
    
    return render_template('programas.html', carreras=carreras)

# Route to handle form submissions
@app.route('/agregar_programa', methods=['POST'])
def agregar_programa():
    if request.method == 'POST':
        descripcion = request.form['descripcion_carrera']
        conn = db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                # Insert the new program into the database
                cursor.execute("INSERT INTO carrera (descripcion) VALUES (?)", (descripcion,))
                conn.commit()
            except sqlite3.IntegrityError:
                # This handles the case where the description already exists (UNIQUE constraint)
                return "Error: Este programa ya existe. Por favor, intente con uno diferente."
            except sqlite3.Error as e:
                print(f"Error adding program: {e}")
                return "Error al agregar el programa."
            finally:
                conn.close()

    # Redirect to the programs page to show the updated list
    return programas()

# Other routes (index, mision, vision) remain the same
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mision')
def mision():
    return render_template('mision.html')

@app.route('/vision')
def vision():
    return render_template('vision.html')

if __name__ == '__main__':
    # It's a good practice to initialize the DB here if it's not done yet
    db.init_db()
    app.run(debug=True)