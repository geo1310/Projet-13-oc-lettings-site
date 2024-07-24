import pytest
from django.contrib.auth.models import User

from ..models import Profile


@pytest.mark.django_db
def test_profile_model():
    """
    Teste la méthode __str__ du modèle Profile.

    Crée un utilisateur et un profil associé dans la base de données de test,
    puis vérifie que la représentation en chaîne du profil correspond au nom d'utilisateur
    de l'utilisateur.

    Assertions :
    - Vérifie que str(profile) retourne le nom d'utilisateur de l'utilisateur créé.
    """

    user = User.objects.create_user(
        username="testuser", email="test@example.com", password="password"
    )
    profile = Profile.objects.create(user_id=1, favorite_city="city")
    expected_value = user.username
    assert str(profile) == expected_value
