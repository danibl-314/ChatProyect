import sqlite3
import os

DATABASE = 'sisemasexp.db'

# Define el directorio base donde se encuentra este script (database.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_connection():
    # ... (Tu código de conexión) ...
    conn = None
    try:
        # Usa os.path.join para construir la ruta completa de la DB
        db_path = os.path.join(BASE_DIR, DATABASE) 
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def init_db():
    conn = create_connection()
    if conn:
        try:
            # Usa os.path.join para construir la ruta completa del script SQL
            sql_file_path = os.path.join(BASE_DIR, 'sentencias.sql') 
            
            with open(sql_file_path, 'r') as f:
                sql_script = f.read()
            conn.executescript(sql_script)
            conn.commit()
            print("Database initialized successfully.")
        except FileNotFoundError:
            print(f"Error: El archivo 'sentencias.sql' no se encuentra en {BASE_DIR}")
        except sqlite3.Error as e:
            print(f"Error during database initialization: {e}")
        finally:
            conn.close()

if __name__ == '__main__':
    init_db()
    
    # En database.py

# ... (Tu código existente) ...

def get_carrera(carrera_id):
    """Obtiene una carrera por su ID."""
    conn = create_connection()
    carrera = None
    if conn:
        try:
            carrera = conn.execute("SELECT * FROM carrera WHERE id = ?", (carrera_id,)).fetchone()
        except sqlite3.Error as e:
            print(f"Error al obtener carrera: {e}")
        finally:
            conn.close()
    return carrera

def update_carrera(carrera_id, new_descripcion):
    """Actualiza la descripción de una carrera."""
    conn = create_connection()
    success = False
    if conn:
        try:
            conn.execute("UPDATE carrera SET descripcion = ? WHERE id = ?", (new_descripcion, carrera_id))
            conn.commit()
            success = True
        except sqlite3.Error as e:
            print(f"Error al actualizar carrera: {e}")
        finally:
            conn.close()
    return success

def delete_carrera(carrera_id):
    """Elimina una carrera por su ID."""
    conn = create_connection()
    success = False
    if conn:
        try:
            conn.execute("DELETE FROM carrera WHERE id = ?", (carrera_id,))
            conn.commit()
            success = True
        except sqlite3.Error as e:
            print(f"Error al eliminar carrera: {e}")
        finally:
            conn.close()
    return success

# ... (Tu código existente) ...