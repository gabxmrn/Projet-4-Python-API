import tkinter as tk
from tkinter import ttk
import threading
import webbrowser
from flask import Flask, request, jsonify
import API_1.Page_HTML1 as Page_HTML1
import API_2.Page_HTML2 as Page_HTML2
from API_2.Inputs_API2 import Inputs_API2
import API_3.Page_HTML3 as Page_HTML3


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
        self.start_flask_server(5001, project)
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

        # TODO: Code exécuté par le bouton de l'API 1

        # Code exécuté par le bouton de l'API 2
        @app.route('/run_code_api2', methods=['POST'])
        def run_code_api2():
            if request.method == 'POST':
                # Récupération des données
                data = request.get_json()
                print(data)

                # Traitement des données
                input_api2 = Inputs_API2(data)
                if input_api2.verif_params():
                    opt = input_api2.traitement_params()

                    # Output paramètres dans la page HTML
                    html_content = f"<p>Importation et traitement des données réussis.</p>"
                    html_content += "<p>Paramètres sélectionnés :</p>"
                    html_content += "<ul>"
                    for key, value in opt.items():
                        html_content += f"<li>{key}: {value}</li>"
                    html_content += "</ul>"
                    html_content += "<p>La fonction a été exécutée.</p>"

                    return html_content

            return jsonify({"error": "Method not allowed"}), 405
        
        # TODO: Code exécuté par le bouton de l'API 3
