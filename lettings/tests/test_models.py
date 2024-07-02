import pytest
from ..models import Address, Letting


@pytest.mark.django_db
def test_address_model():

    address = Address.objects.create(
        number=100, street="street", city="city", state="ST", zip_code=1234, country_iso_code="abc"
    )
    expected_value = "100 street"
    assert str(address) == expected_value


@pytest.mark.django_db
def test_letting_model():

    address = Address.objects.create(
        number=100, street="street", city="city", state="ST", zip_code=1234, country_iso_code="abc"
    )
    letting = Letting.objects.create(title="title", address_id=1)
    expected_value = "title"
    assert str(letting) == expected_value
    assert address.id == letting.address_id
