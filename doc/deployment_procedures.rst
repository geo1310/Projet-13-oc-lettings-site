Procédures de déploiement et de gestion de l'application
========================================================

L'application possède un workflow ci/cd sur github actions.

Lien vers le workflow : https://github.com/geo1310/Projet-13-oc-lettings-site/actions?query=workflow%3ACI

Le pipeline est conçu pour automatiser le processus de construction, de test et de déploiement de l'application, en garantissant une intégration continue et une livraison continue.

Il est composé de trois étapes :

1. Build : Construction et validation du code.

    *   -> Déclenché sur un Push ou une P.R sur n’importe quelle branche.
    *   Simule l'installation de l'application et des dépendances.
    *   Effectue le lintage du code avec falke8 et black.
    *   Effectue les tests avec une couverture minimum de 80%

2. Deploy Docker : Création et gestion des images Docker.

    *   -> Déclenché sur un Push ou une P.R sur la branche main et aprés la réusssite du build.
    *   Lien vers le Docker Hub : https://hub.docker.com/r/gbriche/oc-lettings-site-web
    *   Les Images Docker sont taguées avec le commit court du push.


3. Deploy Render : Déploiement sur la plateforme Render.

    *   -> Déclenché sur un Push ou une P.R sur la branche main et aprés la réusssite du deploy-docker.
    *   Déploie le projet sur render à l'aide de l'URL webhook de render

    URL Render du projet : https://oc-lettings-site-cuqa.onrender.com
