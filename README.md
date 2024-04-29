# Interface Utilisateur pour l'Intégration des Projets API

Master 272 - Economie & Ingénierie Financière - Année 2023/2024 - Projet : Python API

## Auteurs

Karen Arban, Joudy Benkaddour, Sara Chidawi, Wilhem Fröhlicher, Gabrielle Morin & Clara Noché.

## Aperçu du projet

Cet API a pour objectif de fournir une interface graphique permettant à l'utilisateur de rentrer les différents paramètres requis pour faire fonctionner les trois API développés par les autres groupes de ce projet. Il permet également d'afficher les résultats des API.

## Prérequis

Pour lancer ce projet, vous aurez besoin de Python (version 3.8 ou plus).
Les dépendances spécifiques tels que Flask et Tkinter sont également nécessaires au bon fonctionnement du projet et peuvent être installées via pip.
Pour installer ces dépendances, veuillez utiliser la ligne de commande suivante : ``` pip install requirements.txt ```

## Fonctionnalités 

Lorsque l'utilisateur lance l'application, une fenêtre graphique s'ouvre avec trois boutons, chacun représentant un projet différent :
- Projet 1 : API pour le backtesting de stratégies de trading algorithmique,
- Projet 2 : Création d’analytics de trading personnalisés via API,
- Projet 3 : API d’uniformisation pour les échanges de cryptomonnaies.

Pour le projet 1:

Si l'utilisateur a sélectionné le projet 1, une page HTML s'ouvre et il est ainsi possible de remplir les inputs du projet. Le bouton "Importation des paramètres" permet de visualiser les inputs saisis dans la console. Le bouton "Récupération des outputs" permet d'appeler une API qui se substituera aux APIs des projets de nos camarades des autres groupes afin de récupérer des outputs de même nature. Cette API se situe dans le script API_Global, et est appelée grâce à la fonction projet_1_outputs_api. Il est ainsi possible de modifier le contenu de cette fonction une fois que le projet "API pour le backtesting de stratégies de trading algorithmique" sera finalisé par nos camarades. Les outpus s'affichent sur la même page HTML que les inputs.


## Exécution

Pour lancer ce projet, exécutez le code dans le fichier Main. Vous pourrez alors sélectionner l'API que vous voulez lancer !
