# Generated by Django 5.0.6 on 2024-07-01 15:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("lettings", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="address",
            options={"verbose_name_plural": "addresses"},
        ),
    ]
