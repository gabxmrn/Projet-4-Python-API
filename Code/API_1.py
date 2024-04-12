import tkinter as tk

class API1(tk.Tk):
    """
    Classe qui créée l'interface utilisateur principal et permet de sélectionner l'API du projet à lancer.

    Attributes:
        None
    """
    def __init__(self):
        """
        Initialise la fenêtre de sélection de projet.

        Args:
            self: Instance de la classe Application.

        Returns:
            None
        """
        super().__init__()
        self.title("API pour Backtesting de Stratégies de Trading Algorithmique")
        self.geometry("650x150")
        
        self.create_widgets()

    
    def create_widgets(self):
        """
        Crée les boutons pour chaque projet et les ajoute à la fenêtre.

        Args:
            self: Instance de la classe Application.

        Returns:
            None
        """
        grand_font = ("Helvetica", 12)

        '''
        self.bouton_projet1 = tk.Button(self, 
                                        text="API pour Backtesting de Stratégies de Trading Algorithmique", 
                                        font=grand_font)
        self.bouton_projet1.pack(pady=5)
        '''
        self.text_projet1 = tk.Label(self, 
                                   text="coucou", 
                                   font=grand_font)
        
        self.text_projet1.pack(pady=5)


"""
       Modèle de requête suivi par l'utilisateur :

       - func_strat : La fonction de trading en str renvoyant un poids pour chaque actif à chaque date.
       - requirements : Liste des imports nécessaires.
       - tickers : Liste des tickers considérés.
       - dates_calibration : Dates pour calibrer la fonction de stratégie.
       - dates_test : Dates sur lesquelles on teste la stratégie de trading.
       - interval : Fréquence des observations considérées.
       - amount : Montant initial du portefeuille.
       - rqt_name : Nom de la requête pour identification.

    
    func_strat: str
    requirements: list[str]
    tickers: list[str]
    dates_calibration: list[str]
    interval: str
    amount: str
    rqt_name: str
    # repeat_frequency: str
    """