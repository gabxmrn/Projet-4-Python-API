# Python API : Projet numéros 4 - Interface utilisateur pour l'intégration des projets API

## Membres du Groupe

Karen Arban, Joudy Benkaddour, Sara Chidawi, Wilhem Frölicher, Gabrielle Morin & Clara Noche.

## Répartition du travail

Etant donné que nous devons réaliser une interface utilisateur pour trois projets API avec, pour chacun d'entre eux, une interface gérant les inputs et une les outputs. Nous nous sommes répartis par binômes sur les API, avec une personne s'occupant des inputs et l'autre des outputs.

- Récupération des spécifications des 3 projets au 31 décembre - Gabrielle
- API Global - Gabrielle : permet à l'utilisateur de sélectionner le projet auquel il veut avoir accès.
- API 1 :
  - Inputs -
  - Outpus -
- API 2 :
  - Inputs - Gabrielle
  - Outpus -
- API 3 :
  - Inputs -
  - Outpus -

## Spécification du projet au 31 décembre 2023

### <u>Gabrielle</u>

Nous avons pour objectif de développer une interface permettant :

1/ Inputs
  - Une interface globale qui permet de sélectionner le projet voulu (1, 2 ou 3) ;
  - Pour chaque projet, une interface pour entrer les inputs / sélectionner quoi faire ;
  - Vérification des données : bon format, exceptions.

2/ Outputs
  - Pour chaque API, présentation des outputs (graphiques, tableaux, valeurs, etc.) ;
  - Les outputs seront testés avec des fonctions Mock.

### <u>Joudy</u>

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