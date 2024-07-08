# Étape 1 : Utiliser l'image de base Python 3.11
FROM python:3.11

# Étape 2 : Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Étape 3 : Copier les fichiers de configuration et les dépendances de Poetry
COPY pyproject.toml .
COPY poetry.lock .

# Étape 4 : Installation de Poetry et des dépendances (sans l'environnement racine)
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Étape 5 : Copier le code de l'application dans le conteneur
COPY . .

# Étape 6 : Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Étape 7 : Exposer le port 8000 pour gunicorn
EXPOSE 8000

# Étape 8 : Démarrer l'application Django avec gunicorn
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.asgi:application", "-k", "uvicorn.workers.UvicornWorker"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
