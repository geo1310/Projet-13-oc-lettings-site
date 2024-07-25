# Generated by Django 5.0.6 on 2024-06-28 10:17

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MaxValueValidator(9999)]
                    ),
                ),
                ("street", models.CharField(max_length=64)),
                ("city", models.CharField(max_length=64)),
                (
                    "state",
                    models.CharField(
                        max_length=2,
                        validators=[django.core.validators.MinLengthValidator(2)],
                    ),
                ),
                (
                    "zip_code",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MaxValueValidator(99999)]
                    ),
                ),
                (
                    "country_iso_code",
                    models.CharField(
                        max_length=3,
                        validators=[django.core.validators.MinLengthValidator(3)],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Letting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256)),
                (
                    "address",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lettings.address",
                    ),
                ),
            ],
        ),
    ]
