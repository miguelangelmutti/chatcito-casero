# 💬 Chat en Tiempo Real con Flask-SocketIO

Una aplicación de chat simple y elegante construida con Flask y Flask-SocketIO.

## 📋 Características

- Chat en tiempo real usando WebSockets
- Interfaz moderna y responsiva
- Notificaciones de conexión/desconexión
- Mensajes con timestamp
- Nombres de usuario personalizables

## 🚀 Instalación

1. **Crear un entorno virtual:**
   ```bash
   python -m venv env_chat
   ```

2. **Activar el entorno virtual:**
   - Windows:
     ```bash
     .\env_chat\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source env_chat/bin/activate
     ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Ejecutar la aplicación

```bash
python app.py
```

La aplicación estará disponible en: `http://localhost:5000`

## 📁 Estructura del proyecto

```
chatcito-casero/
│
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Este archivo
│
├── templates/            # Plantillas HTML
│   └── index.html
│
└── static/              # Archivos estáticos
    ├── css/
    │   └── style.css
    └── js/
        └── chat.js
```

## 🛠️ Tecnologías utilizadas

- **Flask**: Framework web
- **Flask-SocketIO**: WebSockets para comunicación en tiempo real
- **Socket.IO**: Biblioteca JavaScript para WebSockets
- **Eventlet**: Servidor WSGI asíncrono

## 📝 Uso

1. Abre la aplicación en tu navegador
2. (Opcional) Escribe tu nombre en el campo "Tu nombre"
3. Escribe tu mensaje
4. Presiona Enter o haz clic en "Enviar"
5. ¡Disfruta chateando en tiempo real!

## 🔧 Configuración

Puedes modificar la configuración en `app.py`:
- `SECRET_KEY`: Cambia la clave secreta por una más segura
- `host` y `port`: Modifica la dirección y puerto del servidor

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso personal y educativo.
