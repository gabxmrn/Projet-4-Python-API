import requests

# Préparer l'URL et les paramètres de la requête
url = "http://127.0.0.1:5000/api/v1/ta/rsi"
params = {
    'tickers': 'BTCUSDT',
    'ohlcv': 'Close',
    'freq': '1d',
    'start_date': '17-08-2020',
    'end_date': '17-08-2021',
    'n': 14
}

#{'fnc': 'fnc1', 'startDate': '2020-08-17', 'endDate': '2021-08-17', 'dataType': ['Close'], 'freq': '1d', 'tickers': 'BTCUSDT'}

# Envoyer la requête GET
response = requests.get(url, params=params)

# Vérifier le statut de la requête et afficher les résultats
if response.status_code == 200:
    print(response.json())
else:
    print("Erreur lors de la requête :", response.text)
