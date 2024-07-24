from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """
    Modèle représentant une adresse physique.

    Attributes:

    - number (PositiveIntegerField): Numéro de l'adresse.
    - street (CharField): Nom de la rue.
    - city (CharField): Ville.
    - state (CharField): État ou province (doit avoir exactement 2 caractères).
    - zip_code (PositiveIntegerField): Code postal.
    - country_iso_code (CharField): Code ISO du pays (doit avoir exactement 3 caractères).
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f"{self.number} {self.street}"

    class Meta:
        verbose_name_plural = "addresses"


class Letting(models.Model):
    """
    Modèle représentant un bien à louer.

    Attributes:

    - title (CharField): Titre du bien.
    - address (OneToOneField): Adresse du bien (relation One-to-One avec le modèle Address).
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
