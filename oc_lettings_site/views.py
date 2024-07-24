import sentry_sdk
from django.shortcuts import render


def index(request):
    """
    Affiche la page d'accueil du site OC Lettings.

    Cette vue rend le template 'oc_lettings_site/index.html'.
    Ce template contient du contenu statique représentant la page d'accueil du site OC Lettings.

    Parameters:

    - request: Objet HttpRequest contenant les données de la requête HTTP.

    Returns:

    - HttpResponse: Renvoie la réponse HTTP rendue à partir du template spécifié.
    """
    return render(request, "oc_lettings_site/index.html")


def custom_handler404(request, exception=None):
    """
    Vue pour gérer les erreurs 404 (Page non trouvée).

    Affiche le template 'oc_lettings_site/404.html' avec un statut HTTP 404.

    Parameters:

    - request: Objet HttpRequest contenant les données de la requête HTTP.
    - exception: L'exception qui a déclenché l'erreur 404 (optionnel).

    Returns:

    - HttpResponse: Renvoie la réponse HTTP rendue à partir du template spécifié
      avec un statut 404.
    """
    sentry_sdk.capture_message("Page non trouvée (404): {}".format(request.path), level="warning")

    return render(request, "oc_lettings_site/404.html", status=404)


def custom_handler500(request):
    """
    Vue pour gérer les erreurs 500 (Erreur interne du serveur).

    Affiche le template 'oc_lettings_site/500.html' avec un statut HTTP 500.

    Parameters:

    - request: Objet HttpRequest contenant les données de la requête HTTP.

    Returns:

    - HttpResponse: Renvoie la réponse HTTP rendue à partir du template spécifié
      avec un statut 500.
    """

    sentry_sdk.capture_exception()

    return render(request, "oc_lettings_site/500.html", status=500)
