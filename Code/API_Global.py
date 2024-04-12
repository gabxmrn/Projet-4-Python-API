import tkinter as tk
from tkinter import ttk
from API_1 import API1


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
        #self.geometry("650x150")
        self.configure(bg="#f0f0f0")
        
        style = ttk.Style(self)
        style.configure("TButton", font=("Helvetica", 12), padding=10)  # Style des boutons
        style.configure("TLabel", font=("Helvetica", 12))  # Style des labels

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
        bouton_couleur = "#4CAF50"

        self.bouton_projet1 = ttk.Button(self, 
                                        text="Projet 1 : API pour Backtesting de Stratégies de Trading Algorithmique", 
                                        command=self.choisir_projet_1,
                                        style="TButton",
                                        cursor="hand2")
        self.bouton_projet1.pack(pady=5)

        self.bouton_projet2 = ttk.Button(self, 
                                        text="Projet 2 : Création d’Analytics de Trading Personnalisés via API", 
                                        command=self.choisir_projet_2,
                                        style="TButton",
                                        cursor="hand2")
        self.bouton_projet2.pack(pady=5)

        self.bouton_projet3 = ttk.Button(self, 
                                        text="Projet 3 : API d’Uniformisation pour Échanges de Cryptomonnaies", 
                                        command=self.choisir_projet_3,
                                        style="TButton",
                                        cursor="hand2")
        self.bouton_projet3.pack(pady=5)

        max_button_width = max(self.bouton_projet1.winfo_reqwidth(),
                               self.bouton_projet2.winfo_reqwidth(),
                               self.bouton_projet3.winfo_reqwidth())
        
        max_button_height = self.bouton_projet1.winfo_reqheight() + self.bouton_projet2.winfo_reqheight() + self.bouton_projet3.winfo_reqheight()
                                
        self.geometry(f"{max_button_width + 40}x{max_button_height + 40}")


    def choisir_projet_1(self):
        # Instanciation
        app = API1()
        app.mainloop()


    def choisir_projet_2(self):
        # Appeler la méthode spécifique pour le Projet 2
        # TO DO
        pass


    def choisir_projet_3(self):
        # Appeler la méthode spécifique pour le Projet 3
        # TO DO
        pass
