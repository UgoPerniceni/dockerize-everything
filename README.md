﻿PROJET :  DOCKERIZE EVERYTHING
================
L'objectif de ce projet est d'industrialiser l'application de votre choix. Industrialiser une application signifie que vous devez installer, paramétrer et optimiser des outils afin qu'une équipe de déveollement de toute taille puisse installer, développer et déployer l'application le plus facilement possible.
Sur ce projet, vous aurez trois tâches principales à effectuer :
- Choisir un workflow Git, justifier votre choix et l’appliquer tout au long de ce projet ;
- Développer une application fonctionnelle minimale, dans le langage de votre choix ;
- Utiliser Docker comme système de conteneurisation afin d’avoir un environnement de développement optimal et de pouvoir déployer votre application facilement.

Des tâches supplémentaires vous seront proposées afin d’assurer une industrialisation optimale de votre application :
- Ajouter des tests logiciels sur votre application ;
- Intégrer un système d’intégration continue (ou CI) afin de tester en continu votre application ;
- Déployer automatiquement votre application sur la plateforme de votre choix (VPS, PaaS, IaaS...)

Versioning
===============

Le Git Flow :
--------------
Nous avons opté pour le gitflow suivant : Feature Branch + Merge Requests afin d'avoir un meilleur suivi des modifications apportées au projet et d'éviter au maximum les conflits.

Les Conventions :
--------------------
Afin que le projet se porte au mieux nous avons décidé d'adopter les conventions suivantes :
 - Commit : [GitKarma](http://karma-runner.github.io/4.0/dev/git-commit-msg.html) & [Gitmoji](https://gitmoji.carloscuesta.me/)
 - Branches : type/InitialePrenomInitialNom-x (exemple -> feat/KM-1)
 - Au moins une approbation sur la merge request, via un "thumb up sign", avant d'effectuer le merge

Fonctionnalités de l’application 
===============

Les fonctionnalités principales:
--------------------
- La CRUD de tâche comprenant un titre, une description et une couleur
- Passer une tâche du status "active" au status "done"
- Consulter la liste des tâches

Les fonctionnalités secondaires:
--------------------
- Trier par numéro et alphabétiquement la liste des tâches
- Restreindre l'affichage des tâches a un certain nombre de tache
- Faire une recherche dans le liste des tâches par le titre et par le numéro

Contribuer 
===============

Clonez le repository : 

    $ git clone https://gitlab.com/KeligMartin/dockerize-everything
    $ cd dockerize-everything

Créez l'image docker et les deux containers : db et server
    
    $ docker-compose up
    
Rendez-vous sur [localhost](http://localhost:8000)

Arrêtez le serveur en pressant les touches "Ctrl" + "C" et relancez le container de la base de données normalement

    $ docker container start dockerize-everything_db_1
    
Relancez le container du serveur web avec la sortie attachée à votre terminal

    $ docker container start -ia dockerize-everything_web_1

Dans un autre terminal, exécutez la commande suivante pour intéragir avec la CLI de votre container :

    $ docker exec -it dockerize-everything_web_1 /bin/bash
    
    
Créez un super user :

    $ cd src
    $ python manage.py createsuperuser

Initialisez votre utilisateur et vous pourrez ajouter de la data sur l'application.