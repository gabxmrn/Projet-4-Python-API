# Fichier "Mock" qui permet de test le code de l'API2
import requests

params = {
    'tickers': 'BTCUSDT',
    'ohlcv': 'Close',
    'freq': '1d',
    'start_date': '17-08-2020',
    'end_date': '17-08-2021',
    'n': 14
}

def RSI_API(data: dict) -> None:
    """
    Simulation d'une fonction.
    
    Parameters:
        data (dict): dictionnaire contenant les données.
    """

    # Préparer l'URL et les paramètres de la requête
    url = "http://127.0.0.1:5000/api/v1/ta/rsi"

    data = params


    # {'fnc': 'fnc1', 'startDate': '2020-08-17', 'endDate': '2021-08-17', 'dataType': ['Close'], 'freq': '1d', 'tickers': 'BTCUSDT'}

    # Envoyer la requête GET
    response = requests.get(url, params=data)

    # Vérifier le statut de la requête et afficher les résultats
    if response.status_code == 200:
        print(response.json())
    else:
        print("Erreur lors de la requête :", response.text)

    print("Exécution de la fonction 1.")


def fnc2(data: dict) -> None:
    """
    Simulation d'une fonction.
    
    Parameters:
        data (dict): dictionnaire contenant les données.
    """
    print("Exécution de la fonction 2.")


def fnc3(data: dict) -> None:
    """
    Simulation d'une fonction.
    
    Parameters:
        data (dict): dictionnaire contenant les données.
    """
    print("Exécution de la fonction 3.")

RSI_API(params)