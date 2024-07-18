FROM python:3.11

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --without dev,docs --no-interaction --no-ansi

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
