import sqlite3
from datetime import datetime, date
import threading

# Lock para manejar concurrencia en SQLite
db_lock = threading.Lock()

DB_NAME = 'chat.db'

def init_db():
    """Inicializa la base de datos y crea la tabla de mensajes si no existe."""
    with db_lock:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                text TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                date TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Crear índice en la columna date para búsquedas más rápidas
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_date ON messages(date)
        ''')
        
        conn.commit()
        conn.close()
        
        print('✅ Base de datos inicializada correctamente')

def save_message(username, text, timestamp):
    """Guarda un mensaje en la base de datos."""
    today = date.today().isoformat()  # Formato: YYYY-MM-DD
    
    with db_lock:
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO messages (username, text, timestamp, date)
                VALUES (?, ?, ?, ?)
            ''', (username, text, timestamp, today))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f'❌ Error al guardar mensaje: {e}')
            return False

def get_today_messages():
    """Obtiene todos los mensajes del día actual."""
    today = date.today().isoformat()
    
    with db_lock:
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT username, text, timestamp
                FROM messages
                WHERE date = ?
                ORDER BY created_at ASC
            ''', (today,))
            
            messages = cursor.fetchall()
            conn.close()
            
            # Convertir a formato de diccionario
            return [
                {
                    'username': msg[0],
                    'text': msg[1],
                    'timestamp': msg[2]
                }
                for msg in messages
            ]
        except Exception as e:
            print(f'❌ Error al obtener mensajes: {e}')
            return []

def clean_old_messages():
    """Elimina los mensajes que no son del día actual."""
    today = date.today().isoformat()
    
    with db_lock:
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            
            cursor.execute('''
                DELETE FROM messages
                WHERE date != ?
            ''', (today,))
            
            deleted_count = cursor.rowcount
            conn.commit()
            conn.close()
            
            if deleted_count > 0:
                print(f'🗑️  Se eliminaron {deleted_count} mensajes antiguos')
            
            return deleted_count
        except Exception as e:
            print(f'❌ Error al limpiar mensajes antiguos: {e}')
            return 0

def get_message_count():
    """Obtiene el número total de mensajes en la base de datos."""
    with db_lock:
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            
            cursor.execute('SELECT COUNT(*) FROM messages')
            count = cursor.fetchone()[0]
            
            conn.close()
            return count
        except Exception as e:
            print(f'❌ Error al contar mensajes: {e}')
            return 0
