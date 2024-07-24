import logging

from django.shortcuts import get_object_or_404, render

from lettings.models import Letting

logger = logging.getLogger("lettings")


def index(request):
    """
    Vue pour la page d'accueil de l'application des locations.

    Cette vue récupère toutes les locations de la base de données et rend le template index.
    En cas d'erreur, elle renvoie le template 404.html.

    Args:

    - request (HttpRequest): L'objet de la requête HTTP.

    Returns:

    - HttpResponse: La réponse HTTP avec le contenu HTML de la page d'accueil,
    - le template 404.html en cas d'erreur.
    """
    try:
        lettings_list = Letting.objects.all()
        if not lettings_list.exists():
            logger.warning("Aucunes locations trouvées dans la base de données.")
        else:
            logger.info(f"Nombre de locations récupérées: {lettings_list.count()}")
        context = {"lettings_list": lettings_list}
        return render(request, "lettings/index.html", context)
    except Exception as e:
        logger.error(f"Erreur lors du chargement des locations: {e}")
        return render(request, "oc_lettings_site/404.html", status=404)


def letting(request, letting_id):
    """
    Vue pour la page de détail d'une location.

    Cette vue récupère la location par son ID et rend le template de la location avec ses détails.
    En cas d'erreur, elle renvoie le template 404.html.

    Args:

    - request (HttpRequest): L'objet de la requête HTTP.
    - letting_id (int): L'ID de la location à récupérer.

    Returns:

    - HttpResponse: La réponse HTTP avec le contenu HTML de la page de détail de la location,
    - le template 404.html en cas d'erreur.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        logger.info(f"Location trouvée: {letting.title}")
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "lettings/letting.html", context)
    except Exception as e:
        logger.error(f"Erreur lors de la récupération de la location avec l'ID {letting_id}: {e}")
        return render(request, "oc_lettings_site/404.html", status=404)
