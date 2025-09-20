import sqlite3

DATABASE = 'sisemasexp.db'

def create_connection():
    """Create a connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # This allows you to access columns by name
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def init_db():
    """Initializes the database by running the SQL script."""
    conn = create_connection()
    if conn:
        try:
            with open('sentencias.sql', 'r') as f:
                sql_script = f.read()
            conn.executescript(sql_script)
            conn.commit()
            print("Database initialized successfully.")
        except sqlite3.Error as e:
            print(f"Error during database initialization: {e}")
        finally:
            conn.close()

if __name__ == '__main__':
    init_db()