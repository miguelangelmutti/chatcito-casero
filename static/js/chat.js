// Conectar al servidor Socket.IO
const socket = io();

// Elementos del DOM
const messagesContainer = document.getElementById('messages');
const messageInput = document.getElementById('message');
const usernameInput = document.getElementById('username');

// Conectar al servidor
socket.on('connect', () => {
    console.log('Conectado al servidor');
});

// Recibir mensajes
socket.on('message', (data) => {
    displayMessage(data);
});

// Enviar mensaje
function sendMessage() {
    const message = messageInput.value.trim();
    const username = usernameInput.value.trim() || 'Anónimo';
    
    if (message === '') {
        return;
    }
    
    const data = {
        username: username,
        text: message,
        timestamp: new Date().toLocaleTimeString('es-ES', { 
            hour: '2-digit', 
            minute: '2-digit' 
        })
    };
    
    socket.emit('message', data);
    messageInput.value = '';
    messageInput.focus();
}

// Mostrar mensaje en el chat
function displayMessage(data) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message';
    
    messageDiv.innerHTML = `
        <span class="username">${escapeHtml(data.username)}:</span>
        <span class="text">${escapeHtml(data.text)}</span>
        <span class="timestamp">${data.timestamp}</span>
    `;
    
    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

// Manejar Enter para enviar mensaje
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

// Escapar HTML para prevenir XSS
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, (m) => map[m]);
}

// Desconexión
socket.on('disconnect', () => {
    console.log('Desconectado del servidor');
});
