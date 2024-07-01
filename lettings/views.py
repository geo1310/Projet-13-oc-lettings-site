from django.shortcuts import render
from lettings.models import Letting


def index(request):
    """
    Fonction de vue pour la page d'accueil de l'application des locations.

    Récupère toutes les locations de la base de données et rend le template index.

    Args:
        request: L'objet de la requête HTTP.

    Returns:
        HttpResponse: HTML rendu de la page d'accueil avec la liste des locations.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Fonction de vue pour la page de détail d'une location.

    Récupère la location par son ID et rend le template de la location avec ses détails.

    Args:
        request: L'objet de la requête HTTP.
        letting_id: L'ID de la location à récupérer.

    Returns:
        HttpResponse: HTML rendu de la page de détail de la location avec le titre et l'adresse
        de la location.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
