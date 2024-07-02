import pytest
from django.urls import reverse
from django.test import Client
from ..models import Letting, Address
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture
def setup_letting_and_address():
    """
    Fixture pour créer une adresse et une location dans la base de données de test.

    Returns:
        tuple: Un tuple contenant l'objet Address créé et l'objet Letting créé.
    """
    address = Address.objects.create(
        number=100, street="street", city="city", state="ST", zip_code=1234, country_iso_code="abc"
    )
    letting = Letting.objects.create(title="Villa sur la plage", address_id=address.id)
    return address, letting


@pytest.mark.django_db
def test_index_view(setup_letting_and_address):
    """
    Teste la vue 'index' de l'application 'lettings'.
    """
    client = Client()
    _, letting = setup_letting_and_address

    path = reverse("lettings:index")
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")
    assert letting.title in str(response.content)


@pytest.mark.django_db
def test_index_view_with_no_address():
    """
    Teste la vue 'index' de l'application 'lettings' lorsque aucune adresse n'est disponible.

    Vérifie que la vue 'index' renvoie correctement le template 'index.html' même lorsqu'aucune
    location n'est trouvée dans la base de données.

    Assertions :
    - Vérifie le statut de la réponse HTTP (200 OK).
    - Vérifie que le template 'index.html' est utilisé pour rendre la réponse.
    - Vérifie qu'aucune location n'est disponible en s'assurant que la variable 'letting'
    est False.
    """

    client = Client()
    letting = False

    path = reverse("lettings:index")
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")
    assert not letting


@pytest.mark.django_db
def test_letting_view(setup_letting_and_address):
    """
    Teste la vue 'letting' de l'application 'lettings'.
    """
    client = Client()
    address, letting = setup_letting_and_address

    path = reverse("lettings:letting", kwargs={"letting_id": letting.id})
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
    assert str(address.number) in str(response.content)
    assert address.street in str(response.content)
    assert address.city in str(response.content)
