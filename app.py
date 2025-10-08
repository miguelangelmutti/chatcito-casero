from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from database import init_db, save_message, get_today_messages, clean_old_messages

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu-clave-secreta-aqui'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')

# Inicializar la base de datos al arrancar la aplicación
init_db()
clean_old_messages()  # Limpiar mensajes de días anteriores al iniciar

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Cliente conectado')
    # Enviar historial de mensajes del día al nuevo cliente
    messages = get_today_messages()
    emit('history', messages)
    print(f'📤 Enviado historial de {len(messages)} mensajes al cliente')

@socketio.on('disconnect')
def handle_disconnect():
    print('Cliente desconectado')

@socketio.on('message')
def handle_message(data):
    print(f'Mensaje recibido: {data}')
    
    # Guardar el mensaje en la base de datos
    save_message(data['username'], data['text'], data['timestamp'])
    
    # Broadcast el mensaje a todos los clientes conectados
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    print('🚀 Servidor iniciado en http://localhost:5000')
    print('💡 Usando gevent como servidor asíncrono')
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
