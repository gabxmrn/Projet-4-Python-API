import matplotlib.pyplot as plt
from datetime import datetime


class Outputs_API2:
    """Classe pour générer les outputs de l'API2.
    """

    def __init__(self, data: list[dict], indicator: str) -> None:
        """Initialise un objet de la classe Outputs_API2. 
        Cette classe est valable pour les données récupérées en temps réelles et historiquement.

        Args:
            data (list[dict]): données à représenter graphique.
            indicator (str): indicateur qui est représenté graphiquement.

        Raises:
            ValueError: Si l'indicateur a représenté est invalide.
        """
        self.__data = data

        if indicator in ["SMA", "EMA", "MACD", "RSI", "BBANDS"]:
            self.__indic = indicator
        else:
            raise ValueError("Erreur : entrez un indicateur valide (SMA, EMA, MACD, RSI, BBANDS).")


    def plot_indicator(self) -> None:
        """Fonction qui représente graphique les indicateurs.
        """
        
        tickers = set([key.split('-')[0] for key in self.__data[0].keys() if key != "Time"])
        times = [datetime.strptime(entry["Time"], "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y") for entry in self.__data]

        plt.figure(figsize=(10, 6))

        for ticker in tickers:
            if self.__indic == "SMA":
                ticker_sma = [entry[f"{ticker}-Close-Sma"] for entry in self.__data]
                ticker_volume_sma = [entry[f"{ticker}-Volume-Sma"] for entry in self.__data]
                
                plt.plot(times, ticker_sma, marker='o', label=f'{ticker} Close SMA')
                plt.plot(times, ticker_volume_sma, marker='o', label=f'{ticker} Volume SMA')

            elif self.__indic == "EMA":
                ticker_ema = [entry[f"{ticker}-Close-Ema"] for entry in self.__data]
                ticker_volume_ema = [entry[f"{ticker}-Volume-Ema"] for entry in self.__data]
                
                plt.plot(times, ticker_ema, marker='o', label=f'{ticker} Close EMA')
                plt.plot(times, ticker_volume_ema, marker='o', label=f'{ticker} Volume EMA')

            elif self.__indic == "MACD":
                ticker_macd = [entry[f"{ticker}-Macd"] for entry in self.__data]
                ticker_signal = [entry[f"{ticker}-Signal"] for entry in self.__data]
                
                plt.plot(times, ticker_macd, marker='o', label=f'{ticker} MACD')
                plt.plot(times, ticker_signal, marker='o', label=f'{ticker} Signal')

            elif self.__indic == "RSI":
                ticker_rsi = [entry[f"{ticker}-Rsi"] for entry in self.__data]
                
                plt.plot(times, ticker_rsi, marker='o', label=f'{ticker} RSI')

            elif self.__indic == "BBANDS":
                ticker_Lb = [entry[f"{ticker}-Lb"] for entry in self.__data]
                ticker_Ma = [entry[f"{ticker}-Ma"] for entry in self.__data]
                ticker_Ub = [entry[f"{ticker}-Ub"] for entry in self.__data]
                
                plt.plot(times, ticker_Lb, marker='o', label=f'{ticker} Lb')
                plt.plot(times, ticker_Ma, marker='o', label=f'{ticker} Ma')
                plt.plot(times, ticker_Ub, marker='o', label=f'{ticker} Ub')

        # Mise en forme du graphique
        plt.xlabel('Temps')

        if self.__indic == "SMA":
            plt.ylabel('SMA')
            plt.title('Moyenne Mobile Simple')
        elif self.__indic == "EMA":
            plt.ylabel('EMA')
            plt.title('Moyenne Mobile Exponentielle')
        elif self.__indic == "MACD":
            plt.ylabel('MACD')
            plt.title('Moving Average Convergence Divergence')
        elif self.__indic == "RSI":
            plt.ylabel('RSI')
            plt.title('Indicateur de Force Relative')
        elif self.__indic == "BBANDS":
            plt.ylabel('BBANDS')
            plt.title('Bandes de Bollinger')
            
        plt.legend()
        plt.tight_layout()
        plt.show()
