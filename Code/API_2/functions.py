# Fichier "Mock" qui permet de test le code de l'API2
import requests
from API_2.Outputs_API2 import Outputs_API2


def test(data: dict) -> None:
    """
    Simulation d'une fonction personnalisée.
    
    Parameters:
        data (dict): dictionnaire contenant les données.
    """
    print("Exécution de la fonction personnalisée.")


def SMA_API(data: dict) -> None:
    """
    Simulation de la fonction de l'API2 qui calcule les SMA.
    
    Parameters:
        data (dict): dictionnaire contenant les données.
    """
    sma = [
        { "Time": "2024-04-28 00:00:00",
            "BTC-Close-Sma": 62000.0, "BTC-Volume-Sma": 10000.0,
            "ETH-Close-Sma": 50000.0, "ETH-Volume-Sma": 8000.0
        },
        { "Time": "2024-04-29 00:00:00",
            "BTC-Close-Sma": 61000.0, "BTC-Volume-Sma": 9500.0,
            "ETH-Close-Sma": 49000.0, "ETH-Volume-Sma": 8500.0
        },
        { "Time": "2024-04-30 00:00:00",
            "BTC-Close-Sma": 60000.0, "BTC-Volume-Sma": 9200.0,
            "ETH-Close-Sma": 51000.0, "ETH-Volume-Sma": 8700.0
        },
        { "Time": "2024-05-01 00:00:00",
            "BTC-Close-Sma": 61000.0, "BTC-Volume-Sma": 9300.0,
            "ETH-Close-Sma": 54000.0, "ETH-Volume-Sma": 8400.0
        },
        { "Time": "2024-05-02 00:00:00",
            "BTC-Close-Sma": 62000.0, "BTC-Volume-Sma": 9500.0,
            "ETH-Close-Sma": 53000.0, "ETH-Volume-Sma": 8300.0
        }
    ]
    
    # Représentation graphique
    output = Outputs_API2(sma,"SMA")
    output.plot_indicator() 


def EMA_API(data: dict) -> None:
    """
    Simulation de la fonction de l'API2 qui calcule les EMA.
    
    Parameters:
        data (dict): dictionnaire contenant les données.
    """
    ema = [
        { "Time": "2024-04-28 00:00:00",
            "BTC-Close-Ema": 62000.0, "BTC-Volume-Ema": 10000.0,
            "ETH-Close-Ema": 50000.0, "ETH-Volume-Ema": 8000.0,
        },
        { "Time": "2024-04-29 00:00:00",
            "BTC-Close-Ema": 61000.0, "BTC-Volume-Ema": 9500.0,
            "ETH-Close-Ema": 49000.0, "ETH-Volume-Ema": 8500.0,
        },
        { "Time": "2024-04-30 00:00:00",
            "BTC-Close-Ema": 60000.0, "BTC-Volume-Ema": 9200.0,
            "ETH-Close-Ema": 51000.0, "ETH-Volume-Ema": 8700.0,
        },
        { "Time": "2024-05-01 00:00:00",
            "BTC-Close-Ema": 61000.0, "BTC-Volume-Ema": 9300.0,
            "ETH-Close-Ema": 54000.0, "ETH-Volume-Ema": 8400.0,
        },
        { "Time": "2024-05-02 00:00:00",
            "BTC-Close-Ema": 62000.0, "BTC-Volume-Ema": 9500.0,
            "ETH-Close-Ema": 53000.0, "ETH-Volume-Ema": 8300.0,
        }
    ]

    # Représentation graphique
    output = Outputs_API2(ema,"EMA")
    output.plot_indicator() 


def MACD_API(data: dict) -> None:
    """
    Simulation de la fonction de l'API2 qui calcule les MACD.
    
    Parameters:
        data (dict): dictionnaire contenant les données.
    """
    macd = [
        { "Time": "2024-04-28 00:00:00",
            "BTC-Macd": 200.0, "BTC-Signal": 180.0,
            "ETH-Macd": 120.0, "ETH-Signal": 90.0
        },
        { "Time": "2024-04-29 00:00:00",
            "BTC-Macd": 210.0, "BTC-Signal": 190.0,
            "ETH-Macd": 110.0, "ETH-Signal": 80.0
        },
        { "Time": "2024-04-30 00:00:00", 
            "BTC-Macd": 190.0, "BTC-Signal": 185.0,
            "ETH-Macd": 90.0, "ETH-Signal": 90.0
        },
        { "Time": "2024-05-01 00:00:00",
            "BTC-Macd": 180.0, "BTC-Signal": 180.0,
            "ETH-Macd": 85.0, "ETH-Signal": 95.0
        },
        { "Time": "2024-05-02 00:00:00",
            "BTC-Macd": 170.0, "BTC-Signal": 175.0,
            "ETH-Macd": 95.0, "ETH-Signal": 90.0
        }
    ]
    
    # Représentation graphique
    output = Outputs_API2(macd,"MACD")
    output.plot_indicator() 


def RSI_API(data: dict) -> None:
    """
    Simulation de la fonction de l'API2 qui calcule les RSI.
    
    Parameters:
        data (dict): dictionnaire contenant les données.
    """

    rsi = [
        { "Time": "2024-04-28 00:00:00",
            "BTC-Rsi": 70.0, "ETH-Rsi": 40.0
        },
        { "Time": "2024-04-29 00:00:00",
            "BTC-Rsi": 72.0, "ETH-Rsi": 47.0
        },
        { "Time": "2024-04-30 00:00:00",
            "BTC-Rsi": 65.0, "ETH-Rsi": 49.0
        },
        { "Time": "2024-05-01 00:00:00",
            "BTC-Rsi": 68.0, "ETH-Rsi": 53.0
        },
        { "Time": "2024-05-02 00:00:00",
            "BTC-Rsi": 60.0, "ETH-Rsi": 50.0
        }
    ]

    # Représentation graphique
    output = Outputs_API2(rsi,"RSI")
    output.plot_indicator() 


def BBANDS_API(data: dict) -> None:
    """
    Simulation de la fonction de l'API2 qui calcule les BBANDS.
    
    Parameters:
        data (dict): dictionnaire contenant les données.
    """

    bb = [
        { "Time": "2024-04-28 00:00:00",
            "BTC-Lb": 6000.0, "BTC-Ma": 6200.0, "BTC-Ub": 6400.0,
            "ETH-Lb": 3000.0, "ETH-Ma": 3200.0, "ETH-Ub": 3400.0
        },
        { "Time": "2024-04-29 00:00:00",
            "BTC-Lb": 5800.0, "BTC-Ma": 6100.0, "BTC-Ub": 6400.0,
            "ETH-Lb": 2900.0, "ETH-Ma": 3100.0, "ETH-Ub": 3300.0
        },
        { "Time": "2024-04-30 00:00:00",
            "BTC-Lb": 5700.0, "BTC-Ma": 6000.0, "BTC-Ub": 6300.0,
            "ETH-Lb": 2800.0, "ETH-Ma": 3000.0, "ETH-Ub": 3200.0
        },
        { "Time": "2024-05-01 00:00:00",
            "BTC-Lb": 5800.0, "BTC-Ma": 6100.0, "BTC-Ub": 6400.0,
            "ETH-Lb": 2900.0, "ETH-Ma": 3100.0, "ETH-Ub": 3300.0
        },
        { "Time": "2024-05-02 00:00:00",
            "BTC-Lb": 5900.0, "BTC-Ma": 6200.0, "BTC-Ub": 6500.0,
            "ETH-Lb": 3000.0, "ETH-Ma": 3200.0, "ETH-Ub": 3400.0
        }
    ]

    # Représentation graphique
    output = Outputs_API2(bb, "BBANDS")
    output.plot_indicator()
