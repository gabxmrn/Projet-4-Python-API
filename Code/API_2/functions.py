# Fichier "Mock" qui permet de test le code de l'API2
import requests


def test(data: dict) -> None:
    """
    Simulation d'une fonction personnalisée.
    
    Parameters:
        data (dict): dictionnaire contenant les données.
    """
    print("Exécution de la fonction personnalisée.")


def SMA_API(data: dict) -> list[dict[str, float]]:
    """
    Simulation de la fonction de l'API2 qui calcule les SMA.
    
    Parameters:
        data (dict): dictionnaire contenant les données.
    Returns:
            list[dict[str, float]]: liste contenant les données simulées.
    """
    [
    { "Time": "2024-04-28 00:00:00",
        "BTC-Close-Sma": 62000.0, "BTC-Volume-Sma": 10000.0
    },
    { "Time": "2024-04-29 00:00:00",
        "BTC-Close-Sma": 61000.0, "BTC-Volume-Sma": 9500.0
    },
    { "Time": "2024-04-30 00:00:00",
        "BTC-Close-Sma": 60000.0, "BTC-Volume-Sma": 9200.0
    },
    { "Time": "2024-05-01 00:00:00",
        "BTC-Close-Sma": 61000.0, "BTC-Volume-Sma": 9300.0
    },
    { "Time": "2024-05-02 00:00:00",
        "BTC-Close-Sma": 62000.0, "BTC-Volume-Sma": 9500.0
    }
]


def EMA_API(data: dict) -> list[dict[str, float]]:
    """
    Simulation de la fonction de l'API2 qui calcule les EMA.
    
    Parameters:
        data (dict): dictionnaire contenant les données.
    Returns:
            list[dict[str, float]]: liste contenant les données simulées.
    """
    return [
        { "Time": "2024-04-28 00:00:00",
            "BTC-Close-Ema": 62000.0, "BTC-Volume-Ema": 10000.0
        },
        { "Time": "2024-04-29 00:00:00",
            "BTC-Close-Ema": 61000.0, "BTC-Volume-Ema": 9500.0
        },
        { "Time": "2024-04-30 00:00:00",
            "BTC-Close-Ema": 60000.0, "BTC-Volume-Ema": 9200.0
        },
        { "Time": "2024-05-01 00:00:00",
            "BTC-Close-Ema": 61000.0, "BTC-Volume-Ema": 9300.0
        },
        { "Time": "2024-05-02 00:00:00",
            "BTC-Close-Ema": 62000.0, "BTC-Volume-Ema": 9500.0
        }
    ]


def MACD_API(data: dict) -> list[dict[str, float]]:
    """
    Simulation de la fonction de l'API2 qui calcule les MACD.
    
    Parameters:
        data (dict): dictionnaire contenant les données.
    Returns:
            list[dict[str, float]]: liste contenant les données simulées.
    """
    return [
        { "Time": "2024-04-28 00:00:00",
            "BTC-Macd": 200.0, "BTC-Signal": 180.0
        },
        { "Time": "2024-04-29 00:00:00",
            "BTC-Macd": 210.0, "BTC-Signal": 190.0
        },
        { "Time": "2024-04-30 00:00:00", 
            "BTC-Macd": 190.0, "BTC-Signal": 185.0
        },
        { "Time": "2024-05-01 00:00:00",
            "BTC-Macd": 180.0, "BTC-Signal": 180.0
        },
        { "Time": "2024-05-02 00:00:00",
            "BTC-Macd": 170.0, "BTC-Signal": 175.0
        }
    ]


def RSI_API(data: dict) -> list[dict[str, float]]:
    """
    Simulation de la fonction de l'API2 qui calcule les RSI.
    
    Parameters:
        data (dict): dictionnaire contenant les données.
    Returns:
            list[dict[str, float]]: liste contenant les données simulées.
    """

    return [
        { "Time": "2024-04-28 00:00:00",
            "BTC-Rsi": 70.0
        },
        { "Time": "2024-04-29 00:00:00",
            "BTC-Rsi": 72.0
        },
        { "Time": "2024-04-30 00:00:00",
            "BTC-Rsi": 65.0
        },
        { "Time": "2024-05-01 00:00:00",
            "BTC-Rsi": 68.0
        },
        { "Time": "2024-05-02 00:00:00",
            "BTC-Rsi": 60.0
        }
    ]


def BBANDS_API(data: dict) -> list[dict[str, float]]:
    """
    Simulation de la fonction de l'API2 qui calcule les BBANDS.
    
    Parameters:
        data (dict): dictionnaire contenant les données.
    Returns:
            list[dict[str, float]]: liste contenant les données simulées.
    """

    return [
        { "Time": "2024-04-28 00:00:00",
            "BTC-Lb": 60000.0, "BTC-Ma": 62000.0, "BTC-Ub": 64000.0
        },
        { "Time": "2024-04-29 00:00:00",
            "BTC-Lb": 58000.0, "BTC-Ma": 61000.0, "BTC-Ub": 64000.0
        },
        { "Time": "2024-04-30 00:00:00",
            "BTC-Lb": 57000.0, "BTC-Ma": 60000.0, "BTC-Ub": 63000.0
        },
        { "Time": "2024-05-01 00:00:00",
            "BTC-Lb": 58000.0, "BTC-Ma": 61000.0, "BTC-Ub": 64000.0
        },
        { "Time": "2024-05-02 00:00:00",
            "BTC-Lb": 59000.0, "BTC-Ma": 62000.0, "BTC-Ub": 65000.0
        }
    ]

