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
