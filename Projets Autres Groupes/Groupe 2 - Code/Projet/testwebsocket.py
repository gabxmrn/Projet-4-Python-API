import socketio

# Création d'une instance du client SocketIO
sio = socketio.Client()

# Gestionnaire pour les réponses du serveur sur le canal 'rsi_response'
@sio.on('bbands_response')
def on_message(data):
    print('J\'ai reçu une réponse bbands:', data)

# Connexion au serveur WebSocket
sio.connect('http://127.0.0.1:5000/')

# Données pour la requête RSI
data = {
    'tickers': ['BTCUSDT'],
    'freq': '1m',
    'n': 10,
}

# Envoi de la requête RSI au serveur
sio.emit('bbands', data)

# L'appel à sio.wait() est bloquant et maintiendra le client en écoute jusqu'à interruption (Ctrl+C, par exemple)
sio.wait()