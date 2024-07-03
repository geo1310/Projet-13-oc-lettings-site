import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed
from ..models import Profile


@pytest.fixture
def setup_profiles():
    """
    Fixture pour créer des profils dans la base de données de test.

    Returns:
        tuple: Un tuple contenant les objets Profile créés.
    """
    user1 = User.objects.create_user(
        username="user1", email="user1@example.com", password="password1"
    )
    user2 = User.objects.create_user(
        username="user2", email="user2@example.com", password="password2"
    )
    profile1 = Profile.objects.create(user=user1, favorite_city="City1")
    profile2 = Profile.objects.create(user=user2, favorite_city="City2")
    return profile1, profile2


@pytest.mark.django_db
def test_index_view(setup_profiles):
    """
    Teste la vue 'index' de l'application 'profiles'.

    Vérifie que la vue 'index' rend correctement le template 'index.html' avec la liste des profils
    récupérés depuis la base de données de test.

    Assertions :
    - Vérifie le statut de la réponse HTTP (200 OK).
    - Vérifie que le template 'index.html' est utilisé pour rendre la réponse.
    - Vérifie que les profils retournés par la vue sont présents dans le contenu de la réponse.
    """
    client = Client()

    path = reverse("profiles:index")
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")
    for profile in setup_profiles:
        assert str(profile) in str(response.content)


@pytest.mark.django_db
def test_index_view_with_no_profiles():
    """
    Teste la vue 'index' de l'application 'profiles' lorsque aucun profil n'est disponible.

    Vérifie que la vue 'index' renvoie correctement le template 'index.html' même lorsqu'aucun
    profil n'est trouvé dans la base de données.

    Assertions :
    - Vérifie le statut de la réponse HTTP (200 OK).
    - Vérifie que le template 'index.html' est utilisé pour rendre la réponse.
    - Vérifie qu'aucun profil n'est disponible en s'assurant que la variable 'profiles' est False.
    """
    client = Client()

    profiles = False
    path = reverse("profiles:index")
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")
    assert not profiles


@pytest.mark.django_db
def test_profile_view(setup_profiles):
    """
    Teste la vue 'profile' de l'application 'profiles'.

    Vérifie que la vue 'profile' rend correctement le template 'profile.html' avec les détails
    du profil
    récupéré depuis la base de données de test.

    Assertions :
    - Vérifie le statut de la réponse HTTP (200 OK).
    - Vérifie que le template 'profile.html' est utilisé pour rendre la réponse.
    - Vérifie que les détails du profil retournés par la vue sont présents dans le contenu
    de la réponse.
    """
    client = Client()

    username = setup_profiles[0].user.username  # On utilise le premier profil créé pour ce test

    path = reverse("profiles:profile", kwargs={"username": username})
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
    assert str(setup_profiles[0].user.username) in str(response.content)
    assert setup_profiles[0].favorite_city in str(response.content)
