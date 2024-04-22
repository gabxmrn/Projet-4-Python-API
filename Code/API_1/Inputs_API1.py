import re, os
import importlib.util
import datetime as dt


class Inputs_API1:
    """Classe pour gérer les paramètres entrants de l'API 1."""

    def __init__(self, requete: dict) -> None:
        """Initialise un objet Inputs_API1 avec les résultats d'une requête."""
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

        # Contrôle - Montant    
        if 'amt' not in self.__data or self.__data['amt'] is None:
            raise ValueError("Erreur : Veuillez un montant.")

        # Contrôle - Ticker à importer
        if 'dataTicker' not in self.__data or self.__data['dataTicker'] is None:
            raise ValueError("Erreur : Veuillez sélectionner au moins un ticker.")
        
        # Contrôle - Dates sélectionnées (calibrage)
        if 'startDateCal' not in self.__data or self.__data['startDateCal'] is None:
            raise ValueError("Erreur : Veuillez entrer une date de début de calibrage.")
        
        if 'endDateCal' not in self.__data or self.__data['endDateCal'] is None:
            raise ValueError("Erreur : Veuillez entrer une date de fin de calibrage.")
        
        if self.__data['endDateCal'] < self.__data['startDateCal']:
            raise ValueError("Erreur : la date de fin de calibrage doit être après la date de début de calibrage.")

        # Contrôle - Dates sélectionnées (test)
        if 'startDateTest' not in self.__data or self.__data['startDateTest'] is None:
            raise ValueError("Erreur : Veuillez entrer une date de début de test.")
        
        if 'endDateTest' not in self.__data or self.__data['endDateCal'] is None:
            raise ValueError("Erreur : Veuillez entrer une date de fin de test.")
        
        if self.__data['endDateTest'] < self.__data['startDateTest']:
            raise ValueError("Erreur : la date de fin de test doit être après la date de début de test.")

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

        ## Ticker
        ticker_ok = ""
        for t in self.__data['dataTicker']:
            ticker_ok += t[0]

        # Sélection des options
        options = {
            'function': self.__data['fnc'],
            'tickers': ticker_ok,
            'freq': self.__data['freq'],
            'amt': self.__data['amt'],
            'start_date_cal': int(dt.datetime.strptime(self.__data['startDateCal'], "%Y-%m-%d").timestamp()),
            'end_date_cal' : int(dt.datetime.strptime(self.__data['endDateCal'], "%Y-%m-%d").timestamp()),
            'start_date_test': int(dt.datetime.strptime(self.__data['startDateTest'], "%Y-%m-%d").timestamp()),
            'end_date_test' : int(dt.datetime.strptime(self.__data['endDateTest'], "%Y-%m-%d").timestamp())
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