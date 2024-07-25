===========================
Instructions d'installation
===========================

Pour installer et exécuter le projet localement, suivez les étapes suivantes :

Clonez le repository GitHub : https://github.com/geo1310/Projet-13-oc-lettings-site.git

Installation et activation de l'environnement Virtuel et des dépendances
========================================================================
Création de l'environnement virtuel :

```bash
python -m venv .venv
```

Activation de l'environnement virtuel se placer dans le dossier **.venv/scripts** et taper :

```bash
./activate
```

Installation des dependances necessaires au projet avec poetry :

```bash
pip install poetry
```

```bash
poetry install
```

Installation des pré-commit :

```
pre-commit install
```

Les pré-commit effectuent un lintage du code avant chaque commit sur le code.


Pour travailler sans le mode DEBUG ( désactivé par défaut ) en local, collecter les fichiers statics :

```
python manage.py collectstatic --noinput
```

Pour générer la documentation Sphinx en local :

```
poetry run sphinx-build -b html doc/ doc/_build/
```

Usage
=====

Executer le serveur en local :

```
python manage.py runserver
```

- Aller sur http://localhost:8000 dans un navigateur.


Interface d'administration :

- Aller sur http://localhost:8000/admin
- Connectez-vous avec l'utilisateur `admin` , mot de passe `Abc1234!`

Déploiement sur render :
========================

L'application est accessible à l'adresse suivante :  https://oc-lettings-site-cuqa.onrender.com

Interface d'administration : https://oc-lettings-site-cuqa.onrender.com/admin/login/?next=/admin/

Images Docker :
===============

Les images Docker sont taguées avec le commit court.

Lien vers le hub public : https://hub.docker.com/r/gbriche/oc-lettings-site-web

Au lancement d'une image , mettre 8000 au host port.


Tests
=====

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

Journalisation
==============

L'application possède une journalisation sur sentry, enregistrant les exceptions levées et inattendues.

Lien vers sentry : https://oc-student-gbriche.sentry.io/auth/login/oc-student-gbriche/

Compte test sur Sentry pour accéder au logging :

*   Email : `ocstudentgeo@gmail.com`
*   Mot de passe : `Pass_P13_OC_Python`


Selectionner le projet : `python-django`
