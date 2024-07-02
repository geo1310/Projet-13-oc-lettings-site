import pytest
from ..models import Address, Letting


@pytest.mark.django_db
def test_address_model():
    """
    Teste la méthode __str__ du modèle Address.

    Crée une instance de Address dans la base de données de test avec des valeurs spécifiques,
    puis vérifie que la représentation en chaîne de cette instance correspond aux attentes.

    Assertions :
    - Vérifie que str(address) retourne la chaîne attendue "100 street".
    """

    address = Address.objects.create(
        number=100, street="street", city="city", state="ST", zip_code=1234, country_iso_code="abc"
    )
    expected_value = "100 street"
    assert str(address) == expected_value


@pytest.mark.django_db
def test_letting_model():
    """
    Teste la méthode __str__ du modèle Letting.

    Crée une instance de Address et de Letting dans la base de données de test,
    et vérifie que la représentation en chaîne du Letting correspond aux attentes.
    Vérifie également que l'ID de l'adresse associée au Letting est correct.

    Assertions :
    - Vérifie que str(letting) retourne la chaîne attendue "title".
    - Vérifie que letting.address_id correspond à l'ID de l'adresse créée.
    """

    address = Address.objects.create(
        number=100, street="street", city="city", state="ST", zip_code=1234, country_iso_code="abc"
    )
    letting = Letting.objects.create(title="title", address_id=1)
    expected_value = "title"
    assert str(letting) == expected_value
    assert address.id == letting.address_id
