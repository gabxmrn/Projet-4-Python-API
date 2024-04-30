 import tkinter as tk
from tkinter import ttk
import threading
import webbrowser

import requests
from flask import Flask, request, jsonify
import API_1.Page_HTML1 as Page_HTML1
from API_1.Inputs_API1 import Inputs_API1
import API_2.Page_HTML2 as Page_HTML2
from API_2.Inputs_API2 import Inputs_API2
#import API_3.page_HTML3 as Page_HTML3


class Application(tk.Tk):
    """
    Classe qui créée l'interface utilisateur principal et permet de sélectionner l'API du projet à lancer.
    """

    def __init__(self):
        """
        Initialise la fenêtre de sélection de projet.
        """
        super().__init__()
        self.title("Sélection du projet")
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
        """
        self.bouton_projet1 = ttk.Button(self, 
                                        text="Projet 1 : API pour Backtesting de Stratégies de Trading Algorithmique", 
                                        command=self.lancer_projet_1,
                                        style="TButton",
                                        cursor="hand2")
        self.bouton_projet1.pack(pady=5)

        self.bouton_projet2 = ttk.Button(self, 
                                        text="Projet 2 : Création d’Analytics de Trading Personnalisés via API", 
                                        command=self.lancer_projet_2,
                                        style="TButton",
                                        cursor="hand2")
        self.bouton_projet2.pack(pady=5)

        self.bouton_projet3 = ttk.Button(self, 
                                        text="Projet 3 : API d’Uniformisation pour Échanges de Cryptomonnaies", 
                                        command=self.lancer_projet_3,
                                        style="TButton",
                                        cursor="hand2")
        self.bouton_projet3.pack(pady=5)

        max_button_width = max(self.bouton_projet1.winfo_reqwidth(),
                               self.bouton_projet2.winfo_reqwidth(),
                               self.bouton_projet3.winfo_reqwidth())
        
        max_button_height = self.bouton_projet1.winfo_reqheight() + self.bouton_projet2.winfo_reqheight() + self.bouton_projet3.winfo_reqheight()
                                
        self.geometry(f"{max_button_width + 40}x{max_button_height + 40}")


    def lancer_projet_1(self):
        """ Démarre le projet 1 en fermant la fenêtre actuelle et en lançant le serveur Flask sur le port 5000. """
        project = 1
        self.destroy()
        self.start_flask_server(5000, project)


    def lancer_projet_2(self):
        """ Démarre le projet 2 en fermant la fenêtre actuelle et en lançant le serveur Flask sur le port 5000. """
        project = 2
        self.destroy()
        self.start_flask_server(5027, project)
        pass


    def lancer_projet_3(self):
        """ Démarre le projet 3 en fermant la fenêtre actuelle et en lançant le serveur Flask sur le port 5000. """
        project = 3
        self.destroy()
        self.start_flask_server(5002, project)
        pass


    def start_flask_server(self, port, project_nb):
        """ 
         Démarre un serveur Flask sur le port spécifié et ouvre un navigateur web pour accéder à l'API du projet.

        Args:
            port (int): Le port sur lequel démarrer le serveur Flask.
            project_nb (int): Le numéro du projet à lancer.
        """
        app = Flask(__name__)
        @app.route('/', methods=['GET'])
        
        def index():
            if project_nb == 1:
                return Page_HTML1.construction_API1()
            elif project_nb == 2:
                return Page_HTML2.construction_API2()
            elif project_nb == 3:
                return Page_HTML3.construction_API3()

        threading.Thread(target=lambda: app.run(port=port, debug=False)).start()
        webbrowser.open_new_tab(f'http://127.0.0.1:{port}')

        # Code exécuté par le bouton de l'API 1
        @app.route('/run_code_api1', methods=['POST'])
        def run_code_api1():
            if request.method == 'POST':
                # Récupération des données
                data = request.get_json()

                # Traitement des données
                input_api1 = Inputs_API1(data)
                if input_api1.verif_params():
                    opt = input_api1.traitement_params()

            return jsonify({"error": "Method not allowed"}), 405

        # Code exécuté par le bouton de l'API 2
        @app.route('/run_code_api2', methods=['POST'])
        def run_code_api2():
            if request.method == 'POST':
                # Récupération des données
                data = request.get_json()

                # Traitement des données
                input_api2 = Inputs_API2(data)
                if input_api2.verif_params():
                    opt = input_api2.traitement_params()

            return jsonify({"error": "Method not allowed"}), 405
               
        # TODO: Code exécuté par le bouton de l'API 3
        @app.route('/run_code_api3', methods=['POST'])
        def run_code_api3():
            pass

        # Simulation de l'API du projet 1 pour ressortir les outputs 
        # La réponse de l'API fournit des statistiques et des analyses de performance pour la stratégie testée dans un dictionnaire
        @app.route('/Projet_1_Outputs_API')
        def projet_1_outputs_api():
            # Dictionnaire des outputs 
            output_data = {
                'Rendement Annuel': 1.09906787617619,
                'Volatilite Annuelle': 0.04427079325967763,
                'Ratio de Sharpe': -3.609808326515445,
                'Skewness': 0.9234094592660941,
                'Kurtosis': 10.37351565352118,
                'Semi-Deviation': 0.009548205172359929,
                'VaR Historique': -0.02038805996511345,
                'Drawdown Maximal': -3.187857228514659,
                'Volatilite a la Baisse': 0.19913312424995852,
                'Ratio de Sortino': -0.8025238328989932,
                'Ratio de Calmar': 0.0037046536093212346
            }
            return jsonify(output_data)
        
        
        
