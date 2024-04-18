import re

# TODO: Mise en forme des paramètres appropriée (cf git de Lucas) => conversion dates surtout
# TODO: Affichage des exceptions sur la page HTML plutôt que dans la console ? voir si c'est possible
# TODO: Contrôle de la fonction entrée (faire une classe mock avec des petites fonctions à utiliser)

class Inputs_API2:

    def __init__(self, requete: dict) -> None:
        self.__data = requete

    def verif_params(self) -> bool:

        # TODO: Contrôle - Fonction

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
    
    def traitement_params(self):
        pass