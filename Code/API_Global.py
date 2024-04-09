import tkinter as tk


class Application(tk.Tk):
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
        self.title("Sélection du projet")
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

        self.bouton_projet1 = tk.Button(self, 
                                        text="Projet 1 : API pour Backtesting de Stratégies de Trading Algorithmique", 
                                        command=self.choisir_projet_1,
                                        font=grand_font)
        self.bouton_projet1.pack(pady=5)

        self.bouton_projet2 = tk.Button(self, 
                                        text="Projet 2 : Création d’Analytics de Trading Personnalisés via API", 
                                        command=self.choisir_projet_2,
                                        font=grand_font)
        self.bouton_projet2.pack(pady=5)

        self.bouton_projet3 = tk.Button(self, 
                                        text="Projet 3 : API d’Uniformisation pour Échanges de Cryptomonnaies", 
                                        command=self.choisir_projet_3,
                                        font=grand_font)
        self.bouton_projet3.pack(pady=5)


    def choisir_projet_1(self):
        # Appeler la méthode spécifique pour le Projet 1
        # TO DO
        pass


    def choisir_projet_2(self):
        # Appeler la méthode spécifique pour le Projet 2
        # TO DO
        pass


    def choisir_projet_3(self):
        # Appeler la méthode spécifique pour le Projet 3
        # TO DO
        pass
