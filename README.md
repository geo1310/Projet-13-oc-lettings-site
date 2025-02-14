![image](./doc/_static/images/Orange%20County_Lettings_banner.png)

# OC-LETTINGS-SITE
![Python](https://img.shields.io/badge/python-3.11.x-green.svg)
![Django](https://img.shields.io/badge/django-5.0.6-green.svg)
[![Sentry](https://img.shields.io/badge/Sentry-Enabled-brightgreen.svg)](https://sentry.io)

[![Docker](https://img.shields.io/badge/docker-blue.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![Docker](https://img.shields.io/badge/docker_oc_lettings_site-blue.svg?logo=docker&logoColor=white)](https://hub.docker.com/r/gbriche/oc-lettings-site-web)
[![Render](https://img.shields.io/badge/render-46E3B7?logo=render&logoColor=white)](https://render.com/)
[![Render](https://img.shields.io/badge/render_oc_lettings_site-46E3B7?logo=render&logoColor=white)](https://oc-lettings-site-cuqa.onrender.com)

[![pytest](https://img.shields.io/badge/pytest-passing-success)](https://pytest.org)
[![Coverage](https://img.shields.io/badge/coverage-89%25-brightgreen)](https://coverage.readthedocs.io/en/latest/)

[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Flake8](https://img.shields.io/badge/flake8-checked-blueviolet)](https://flake8.pycqa.org/en/latest/)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

![Repo Size](https://img.shields.io/github/repo-size/geo1310/Projet-13-oc-lettings-site)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/geo1310/Projet-13-oc-lettings-site)
[![GitHub Action](https://img.shields.io/github/actions/workflow/status/geo1310/Projet-13-oc-lettings-site/ci-cd.yml
)](https://github.com/geo1310/Projet-13-oc-lettings-site/actions?query=workflow%3ACI)


## Résumé

Site web d'Orange County Lettings.

Orange County Lettings est une start-up dans le secteur de la location de biens immobiliers.

Domaines du site et du déploiement a améliorer et/ou ajouter :


    1. Refonte de l'architecture modulaire dans le repository GitHub ;
    2. Réduction de diverses dettes techniques sur le projet ;
    3. Ajout d'un pipeline CI/CD ainsi que son déploiement ;
    4. Surveillance de l’application et suivi des erreurs via Sentry ;
    5. Création de la documentation technique de l’application avec Read The Docs et Sphinx.

## Documents du Projet


1. __[Site web 2.0 - caracteristiques et ameliorations](doc/_static/Site+web+2.0+-+caractéristiques+et+améliorations.pdf)__

2. __[Configuration Read the Docs Sphinx](doc/_static/Configuration+Read+the+Docs.pdf)__

3. __[Repo d'origine](https://github.com/OpenClassrooms-Student-Center/Projet-13-oc-lettings-site.git)__

4. __[Documentation du projet](http://gbriche-oc-lettings-site.readthedocs.io/)__

## Installation et activation de l'environnement Virtuel et des dépendances
### Création de l'environnement virtuel :
```bash
python -m venv .venv
```
### Activation de l'environnement virtuel se placer dans le dossier **.venv/scripts** et taper :
```bash
./activate
```
### Installation des dependances necessaires au projet avec poetry :
```bash
pip install poetry
poetry install

```

### Installation des pré-commit :

Possibilité de mettre en service des pré-commit.
```
pre-commit install 
```
Les pré-commit effectuent un lintage du code avant chaque commit sur le code.


### Pour travailler sans le mode DEBUG ( désactivé par défaut ) en local, collecter les fichiers statics :

```
python manage.py collectstatic --noinput
```

### Pour générer la documentation Sphinx en local :

```
poetry run sphinx-build -b html doc/ doc/_build/
```

## Usage

### Executer le serveur en local :
```
python manage.py runserver
```
- Aller sur __http://localhost:8000__ dans un navigateur.

    Page d'accueil de l'application :

![image](./doc/_static/images/Orange%20County_Lettings_index_page.png)


### Interface d'administration :

- Aller sur __http://localhost:8000/admin__
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

## Déploiement sur render :

L'application est accessible à l'adresse suivante :  __https://oc-lettings-site-cuqa.onrender.com__

Interface d'administration : __https://oc-lettings-site-cuqa.onrender.com/admin/login/?next=/admin/__

## Images Docker :

Les images Docker sont taguées avec le commit court.

Lien vers le hub public : __https://hub.docker.com/r/gbriche/oc-lettings-site-web__

Au lancement d'une image , mettre 8000 au host port.



## Tests

Pour executer les tests en local, se placer dans le dossier racine du projet :
```
pytest
```
Pour connaitre la couverture totale des tests :
```
pytest --cov=.
```
Pour effectuer un rapport html des tests :
```
pytest --cov=. --cov-report html
```
Lancer index.html du dossier htlmcov

## Journalisation

L'application possède une journalisation sur sentry, enregistrant les exceptions levées et inattendues.

Lien vers sentry : https://oc-student-gbriche.sentry.io/auth/login/oc-student-gbriche/

Compte test sur Sentry pour accéder au logging :

*   __Email :__ `ocstudentgeo@gmail.com`
*   __Mot de passe :__ `Pass_P13_OC_Python`


Selectionner le projet : `python-django`

## CI/CD

L'application possède un workflow ci/cd sur github actions.

Lien vers le workflow : https://github.com/geo1310/Projet-13-oc-lettings-site/actions?query=workflow%3ACI

Le pipeline est conçu pour automatiser le processus de construction, de test et de déploiement de l'application, en garantissant une intégration continue et une livraison continue.

Il est composé de trois étapes :

1. __Build : Construction et validation du code.__

    *   __-> Déclenché sur un Push ou une P.R sur n’importe quelle branche.__
    *   Simule l'installation de l'application et des dépendances.
    *   Effectue le lintage du code avec falke8 et black.
    *   Effectue les tests avec une couverture minimum de 80%

2. __Deploy Docker : Création et gestion des images Docker.__

    *   __-> Déclenché sur un Push ou une P.R sur la branche main et aprés la réusssite du build.__
    *   Lien vers le Docker Hub : https://hub.docker.com/r/gbriche/oc-lettings-site-web
    *   Les Images Docker sont taguées avec le commit court du push.


3. __Deploy Render : Déploiement sur la plateforme Render.__

    *   __-> Déclenché sur un Push ou une P.R sur la branche main et aprés la réusssite du deploy-docker.__
    *   Déploie le projet sur render à l'aide de l'URL webhook de render


## Contribuer

Si vous souhaitez contribuer à ce projet, veuillez suivre ces étapes :

    Ouvrez un problème pour discuter de ce que vous souhaitez changer.
    Fork ce dépôt et créez une branche pour votre contribution.
    Soumettez une demande d'extraction avec vos modifications.
