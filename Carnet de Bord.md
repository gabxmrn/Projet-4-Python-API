# Python API : Projet numéros 4 - Interface utilisateur pour l'intégration des projets API

## Membres du Groupe

Karen Arban, Joudy Benkaddour, Sara Chidawi, Wilhem Frölicher, Gabrielle Morin & Clara Noche.

## Répartition du travail

Etant donné que nous devons réaliser une interface utilisateur pour trois projets API avec, pour chacun d'entre eux, une interface gérant les inputs et une les outputs. Nous nous sommes répartis par binômes sur les API, avec une personne s'occupant des inputs et l'autre des outputs.

- Récupération des spécifications des 3 projets au 31 décembre - Gabrielle
- API Global - Gabrielle & Wilhem : permet à l'utilisateur de sélectionner le projet auquel il veut avoir accès.
- API 1 :
  - Inputs - Wilhem
  - Outputs - Clara
- API 2 :
  - Inputs - Gabrielle
  - Outputs - Joudy
- API 3 :
  - Inputs - Karen
  - Outputs - Sara

## Feuille de route

### Gabrielle

- 28/04/2024
  - Merge de la branche de Joudy (manuellement) ;
  - Inputs de l'API 2 : ajout de la partie sur les données historiques et nettoyage de la partie sur les Websockets (réorganisation, simplification) ;
  - Simulation de fonctions de résultats pour les indicateurs de l'API 2 ;
  - Représentation graphique des résultats de l'API2 ;
  - Dernier docstrings pour les fonctions de l'API2 ;
  - Version prévisionnelle du ReadMe.
- 22/04/2024
  - Corrections sur le carnet de bord ;
  - Ajout d'un message pour indiquer que l'utilisateur doit se rendre dans le terminal en cas d'erreur pour les pages HTML des API 1 et 2 ;
  - Ajout des fonctions flask à exécuter après avoir cliqué sur les boutons des pages HTML des API 1 & 3.
- 19/04/2024 - point sur la dernière semaine
  - Fin de la création de la page HTML pour que l'utilisateur puisse rentrer les inputs de l'API 2 ;
    - Espace pour entrer les tickers, le type de données à récupérer (liste à choix mutlitple), les dates, une fréquence ;
    - Pour les tickers, utilisation de JavaScript pour que le bouton d'espace devienne un / (permet plus tard de séparer la chaîne de caractères créée).
  - Création d'un bouton qui permet d'exécuter un code Python depuis la page HTML ;
  - Récupération des données entrées par l'utilisateur par une requête JSON, envoit vers la classe qui traite l'API 2 ;
  - Contrôle des paramètres entrés par l'utilisateur et renvoie d'un message d'erreur dans le terminal en cas d'erreur ;
  - Si les paramètres séléctionnés sont corrects, alors on les met en forme pour lancer les fonctions (mock) de l'API ;
  - Une fois le code exécuté, message sur la page HTML ;
  - Docstrings pour les classes Inputs_API2 HTMLToolBox et API_2_ContentGenerator ;
  - Fin du codage de la classe HTMLToolBox en ajoutant les fonctions nécessaires pour la génération de la page HTML (ajout au code de base de Wilhem) ;
  - Création d'un README et début de rédaction ;
  - Nombreux tests du code pour vérifier qu'il soit robuste et fonctionne correctement.

### Wilhem (12/04/2024)

- Semaine du 12/04/2024 ;
  - Décision d'utilisation de FlashAPI en plus de boite de dialogue Tkniter créée par Gabrielle ;
  - Création d'un 1 fichier .py par API + une Toolbox pour le template HTML ;
  - Création pour les 3 API de la feuille HTML d'inputs avec a minima le titre pour que tout le monde ait la même structure de code ;
  - Uniformisation des process pour les 3 API ;
- Semaine du 19/04/2024 ;
  - Sur le schéma de ce qui a été fait pour l'API 2 par Gabrielle, création des différentes entrées sur la page HTML pour les inputs ;
  - Tests sur l'API 1 pour s'assurer que les différents controles sont effectivement bons ;
  - Reprise en accord avec Gabrielle d'une partie des codes (pour le bouton et les controles) ;


### Clara
- 20/04/2024
  - Récupération des inputs du projet 1
  - Nombreux Tests afin d'intégrer l'API du projet 1 directement dans notre projet (Tests depuis leur code github : ) / ils ont également intégré une application streamlit dans laquelle un graphique devrait apparaitre
  - Décision de créer une API fictive dans notre projet qui renverra un dictionnaire d'outputs comme dans leur projet initial
- 21/04/2024
  - Création de la route de l'API fictive
- 29/04/2024
  - Update du readme sur les fonctionnalités liées au projet et plus particulièrement liées à l'appel du projet 1 par l'utilisateur
  - Création du bouton "Récupération des outputs" et du dictionnaire qu'il renvoie
  - Test sur github avec l'incorporation du bouton pour la récupération des outputs du projet 1
  - Modification de l'API_Global pour l'ajout de l'API qui simulera le projet 1
  
## Spécification du projet au 31 décembre 2023

### Gabrielle - Récapitulatif global

Nous avons pour objectif de développer une interface permettant :

1/ Inputs

- Une interface globale qui permet de sélectionner le projet voulu (1, 2 ou 3) ;
- Pour chaque projet, une interface pour entrer les inputs / sélectionner quoi faire ;
- Vérification des données : bon format, exceptions.

2/ Outputs

- Pour chaque API, présentation des outputs (graphiques, tableaux, valeurs, etc.) ;
- Les outputs seront testés avec des fonctions Mock.

### Joudy - Premiers tests

Notre projet consiste en la création d'une interface utilisateur qui a pour objectif d'intégrer et de centraliser les fonctionnalités de trois projets distincts développés par d'autres groupes. Notre défi principal réside dans la gestion des API fournies par ces groupes, ainsi que dans leur implémentation au sein d'une API globale. Cette dernière devra être conçue de manière à interagir harmonieusement avec les trois API individuelles à travers une interface unique. De plus, il sera essentiel de mettre en place un système efficace pour la présentation et le stockage des résultats obtenus. Nous devons être capable de réunir ces différents éléments en un ensemble cohérent et fonctionnel.
La complexité de notre tâche dépendra des projets élaborés par les autres équipes. Nous devrons faire preuve d'adaptabilité, notamment en étant capables d'accepter et de traiter une large variété de formats d'entrée, afin de pouvoir interagir efficacement avec les API des autres groupes.
Pour développer notre interface utilisateur en Python, nous avons choisi d'utiliser la librairie Tkinter pour sa simplicité d'utilisation, qui se présente comme un choix idéal compte tenu de notre expérience limitée en matière de création d'interfaces utilisateurs en Python.
Nous avons opté pour la librairie Tkinter après avoir effectué plusieurs tests exploratoires pour évaluer ses capacités. Ces expérimentations nous ont permis de découvrir diverses fonctionnalités, telles que l'ajout d'onglets et la possibilité d'intégrer des graphiques. Un exemple concret de notre utilisation de Tkinter a été un petit projet test. Dans ce dernier, nous avons développé un code permettant d'interagir avec l'API CoinGecko pour récupérer des données de prix, calculer des rendements, et offrir à l'utilisateur la possibilité de définir les pondérations d'un portefeuille composé de BNB, BTC et ETH, ainsi que de choisir les dates de début et de fin. Cette application a servi à réceptionner les données de CoinGecko, fournissant ainsi un exemple simple mais efficace pour comprendre le fonctionnement de Tkinter. L'expérience a démontré que nous pouvons afficher des graphiques. Nous avons également envisagé de structurer notre interface en séparant chaque projet dans un onglet distinct, ce qui devrait contribuer à une organisation claire et une navigation intuitive pour l'utilisateur.
L'objectif est de fournir une expérience utilisateur intuitive et agréable, avec des options flexibles pour afficher les résultats. Selon les préférences et les besoins de l'utilisateur, nous pourrions opter pour des fenêtres pop-up ou intégrer les résultats directement dans l'interface principale.
Pour faciliter la saisie des données, notre interface inclura divers éléments interactifs tels que des boutons et des champs de saisie. Il est essentiel de prêter une attention particulière à la gestion des entrées utilisateur. Nous devrons effectuer de nombreux tests pour garantir que notre interface gère correctement une gamme étendue de données d'entrée, y compris les cas de saisies incorrectes ou inattendues.
En outre, une gestion d'erreurs robuste et efficace sera nécessaire. Cela implique non seulement de capturer et de traiter les erreurs de manière appropriée, mais aussi d'informer l'utilisateur de manière claire et utile lorsqu'une erreur survient. Cette approche garantira non seulement la stabilité de notre application, mais améliorera également l'expérience globale de l'utilisateur en rendant l'interface plus fiable et facile à utiliser.
Effectivement, une attention particulière devra être accordée aux types de données manipulés au sein de notre interface, notamment en ce qui concerne les DataFrames, les dictionnaires et autres structures de données variées. La validation et la vérification des données sont des étapes cruciales pour assurer une interaction harmonieuse et sans erreur avec les API des autres projets.
Avant de transmettre des données à ces API, il est essentiel de s'assurer qu'elles sont dans le format attendu et qu'elles respectent toutes les contraintes ou exigences spécifiques. Cela inclut la vérification des types de données, la validation des formats (comme les formats de date), la gestion des valeurs manquantes, et la vérification de la cohérence des données.
Des tests exhaustifs doivent être réalisés pour s'assurer que notre interface peut gérer une variété de scénarios d'entrée, y compris des cas atypiques ou des saisies utilisateur erronées. Ces tests aideront à identifier et à corriger les problèmes avant que l'interface ne soit utilisée dans un environnement de production. De plus, ces tests contribueront à renforcer la fiabilité et la robustesse de notre application, en assurant que les interactions avec les API externes se déroulent de manière fluide et sans interruption.
Pour répondre efficacement à nos besoins d'adaptabilité, nous adopterons une approche flexible dans le développement de notre interface. L'un des aspects clés de cette stratégie sera d'éviter au maximum l'hardcoding. Nous privilégierons des solutions qui permettent de modifier facilement ces éléments, comme l'utilisation de fichiers de configuration ou de variables facilement ajustables. Cette approche rendra notre application plus flexible et plus facile à maintenir ou à mettre à jour.
En outre, une collaboration étroite avec les autres équipes est essentielle. En dialoguant régulièrement avec elles, nous pourrons anticiper les éventuelles difficultés liées à l'intégration de leurs API. Cela nous permettra d'adapter notre API pour assurer une compatibilité optimale et de planifier des modifications éventuelles. Cette interaction proactive avec les autres groupes contribuera non seulement à une meilleure intégration des différentes composantes du projet, mais favorisera également la création d'une interface utilisateur qui répond efficacement aux besoins et aux attentes de tous les utilisateurs.
Pour une gestion efficace du travail au sein de notre équipe, nous avons décidé d'adopter une stratégie de division claire et structurée. Conformément à notre plan de conception de l'interface utilisateur, nous allons séparer les onglets pour chaque API intégrée. Cette segmentation nous permettra d'organiser notre travail de manière plus ciblée et méthodique.

Pour ce faire, nous constituerons de petits sous-groupes, chacun composé de deux membres, avec pour mission de se concentrer sur une API spécifique. Chaque duo sera responsable de développer l'interaction de l'interface avec une des API externes, en s'assurant que l'intégration est fluide et répond aux exigences fonctionnelles.

En outre, une personne de l'équipe sera désignée pour compiler et unifier l'ensemble des travaux à la fin du processus de développement. Cette personne aura la responsabilité de veiller à la cohérence globale du code, d'assurer l'intégration harmonieuse des différents composants de l'interface et de finaliser l'application pour qu'elle fonctionne comme une entité unifiée. Cette approche garantira non seulement que chaque aspect de l'interface est développé avec attention et expertise, mais également que le produit final est bien coordonné et fonctionne de manière intégrée.
