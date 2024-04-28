import re, os
import importlib.util
import datetime as dt


class Inputs_API2:
    """Classe pour gérer les paramètres entrants de l'API."""

    def __init__(self, requete: dict) -> None:
        """Initialise un objet Inputs_API2 avec les résultats d'une requête."""
        self.__data = requete

    def verif_params(self) -> bool:
        """Vérifie que les paramètres entrés par l'utilisateur (contenus dans la requête) sont correctes.

        Raises:
            ValueError: Si un des paramètres est invalide.
        Returns:
            bool: True si les paramètres sont valides, sinon False.
        """

        # Contrôle - Fonction
        if 'fnc' in self.__data and self.__data['fnc']:
            chemin_complet = os.path.join(os.path.dirname(__file__), 'functions' + '.py')
            if not self.__fonction_existe(self.__data['fnc'], 'functions', chemin_complet):
                print(self.__fonction_existe(self.__data['fnc'], 'functions'))
                raise ValueError("Erreur : la fonction que vous voulez utiliser n'existe pas.")

        # Contrôle - Tickers
        if 'dataType' in self.__data and self.__data['dataType']:
            tickers = self.__data['tickers'].rstrip('/')
            tickers = self.__data['tickers'].split('/')
            for ticker in tickers:
                if not ticker.endswith('USDT'):
                    raise ValueError("Erreur : Chaque crypto-actif doit être an USDT quote-asset.")

        # Contrôle - Type de données à importer
        if 'dataType' not in self.__data or self.__data['dataType'] is None:
            raise ValueError("Erreur : Veuillez sélectionner au moins un type de donées à importer.")
        
        # Contrôle - Dates sélectionnées
        if 'startDate' not in self.__data or self.__data['startDate'] is None:
            raise ValueError("Erreur : Veuillez entrer une date de début.")
        
        if 'endDate' not in self.__data or self.__data['endDate'] is None:
            raise ValueError("Erreur : Veuillez entrer une date de fin.")
        
        if self.__data['endDate'] < self.__data['startDate']:
            raise ValueError("Erreur : la début de fin doit être après la date de début.")

        # Contrôle - Fréquence des données
        if 'freq' in self.__data and self.__data['freq']:
            if not re.search(r's$|min$|h$|d$|w$|m$|y$', self.__data['freq']):
                raise ValueError("Erreur : La fréquence des données doit être une période de temps signifiée par 's', 'min', 'h', 'd', 'w', 'm', ou 'y'.")
        else:
            raise ValueError("Erreur : Veuillez entrer la fréquence d'importation des données.")

        return True
    
    def traitement_params(self) -> dict:
        """Traite les paramètres de la requête pour les formater et exécute la fonction sélectionnée.

        Returns:
            dict: Options formatées pour l'importation de données.
        """
        
        # Formating des paramètres

        ## Tickers
        liste_tick = []
        tickers = self.__data['tickers'].rstrip('/')
        tickers = self.__data['tickers'].split('/')
        for ticker in tickers:
            liste_tick.append(ticker)

        ## Types de données
        type_ok = ""
        for t in self.__data['dataType']:
            type_ok += t[0].lower()

        # Sélection des options
        options = {
            #'function': self.__data['fnc'],
            'tickers': liste_tick,
            'ohlcv': type_ok,
            'freq': self.__data['freq'],
            #'start_date': int(dt.datetime.strptime(self.__data['startDate'], "%Y-%m-%d").timestamp()),
            #'end_date' : int(dt.datetime.strptime(self.__data['endDate'], "%Y-%m-%d").timestamp())
            'start_date': self.__data['startDate'],
            'end_date' : self.__data['endDate']
        }

        # Exécution de la fonction sélectionnée
        chemin_complet = os.path.join(os.path.dirname(__file__), 'functions' + '.py')
        self.__fonction_execution(self.__data['fnc'], 'functions', chemin_complet, options)

        return options

    def __fonction_existe(self, nom_fnc: str, nom_fichier: str, chemin_complet: str) -> bool:
        """Vérifie si la fonction spécifiée existe dans le fichier.

        Args:
            nom_fnc (str): Nom de la fonction à vérifier.
            nom_fichier (str): Nom du fichier contenant les fonctions.
            chemin_complet (str): Chemin complet du fichier.

        Returns:
            bool: True si la fonction existe, sinon False.
        """
        try:
            spec = importlib.util.spec_from_file_location(nom_fichier, chemin_complet)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return hasattr(module, nom_fnc) and callable(getattr(module, nom_fnc))
        except (ImportError, ModuleNotFoundError, AttributeError):
            return False

    def __fonction_execution(self, nom_fnc: str, nom_fichier: str, chemin_complet: str, opt: dict) -> None:
        """Exécute la fonction spécifiée avec les options données.

        Args:
            nom_fnc (str): Nom de la fonction à exécuter.
            nom_fichier (str): Nom du fichier contenant les fonctions.
            chemin_complet (str): Chemin complet du fichier.
            opt (dict): Options à passer à la fonction.
        """
        try:
            spec = importlib.util.spec_from_file_location(nom_fichier, chemin_complet)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Exécution de la fonction
            getattr(module, nom_fnc)(opt)
        
        except FileNotFoundError:
            print("Fichier contenant la fonction introuvable.")