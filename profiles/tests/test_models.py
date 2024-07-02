import pytest
from django.contrib.auth.models import User
from ..models import Profile


@pytest.mark.django_db
def test_profile_model():

    user = User.objects.create_user(
        username="testuser", email="test@example.com", password="password"
    )
    profile = Profile.objects.create(user_id=1, favorite_city="city")
    expected_value = user.username
    assert str(profile) == expected_value
