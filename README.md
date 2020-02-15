PROJET :  DOCKERIZE EVERYTHING
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

LES PRATIQUES GIT
===============

Le Git Flow
--------------
Nous avons opté pour le gitflow suivant : Feature Branch + Merge Requests afin d'avoir un meilleur suivi des modifications apportées au projet et d'éviter au maximum les conflits.

Les Conventions
--------------------
Afin que le projet se porte au mieux nous avons décidé d'adopter les conventions suivantes :
 - Commit : [GitKarma](http://karma-runner.github.io/4.0/dev/git-commit-msg.html) & [Gitmoji](https://gitmoji.carloscuesta.me/)
 - Branches : type/InitialePrenomInitialNom-x (exemple -> feat/KM-1)
