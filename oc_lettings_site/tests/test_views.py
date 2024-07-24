import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_oc_lettings_site_index_view():
    """
    Teste la vue index de l'application OC Lettings Site.

    Crée un client HTTP, récupère l'URL de la vue index, et vérifie que la vue
    retourne le contenu attendu et utilise le bon template.

    Assertions :
    - Vérifie que le contenu "Welcome to Holiday Homes" est présent dans la réponse.
    - Vérifie que le statut de la réponse est 200 (OK).
    - Vérifie que le template 'oc_lettings_site/index.html' est utilisé pour rendre la réponse.
    """
    client = Client()
    path = reverse("index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = "Welcome to Holiday Homes"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "oc_lettings_site/index.html")


@pytest.mark.django_db
def test_handler404():
    """
    Teste le gestionnaire d'erreur 404 de l'application OC Lettings Site.

    Simule une requête vers une URL inexistante et vérifie que l'erreur 404 est retournée
    avec le template 'oc_lettings_site/404.html'.

    Assertions :
    - Vérifie que le statut de la réponse est 404 (Not Found).
    - Vérifie que le template 'oc_lettings_site/404.html' est utilisé pour rendre la réponse.
    """
    client = Client()

    response = client.get("/url-inexistante/")

    assert response.status_code == 404
    assertTemplateUsed(response, "oc_lettings_site/404.html")
