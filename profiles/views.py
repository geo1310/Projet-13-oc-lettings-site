import logging
from django.shortcuts import render, get_object_or_404
from .models import Profile

logger = logging.getLogger("profiles")


def index(request):
    """
    Vue pour la page d'accueil de l'application des profils.

    Cette vue récupère tous les profils de la base de données et rend le template index.
    En cas d'erreur, elle renvoie le template 404.html.

    Args:

    - request (HttpRequest): L'objet de la requête HTTP.

    Returns:

    - HttpResponse: La réponse HTTP avec le contenu HTML de la page d'accueil
    - le template 404.html en cas d'erreur.
    """
    try:
        profiles_list = Profile.objects.all()
        if not profiles_list.exists():
            logger.warning("Aucun profil trouvé dans la base de données.")
        else:
            logger.info(f"Nombre de profils récupérés: {profiles_list.count()}")
        context = {"profiles_list": profiles_list}
        return render(request, "profiles/index.html", context)
    except Exception as e:
        logger.error(f"Erreur lors du chargement des profils: {e}")
        return render(request, "oc_lettings_site/404.html", status=404)


def profile(request, username):
    """
    Vue pour la page de détail d'un profil.

    Cette vue récupère le profil par le nom d'utilisateur et rend le template du profil
    avec ses détails.
    En cas d'erreur, elle renvoie le template 404.html.

    Args:

    - request (HttpRequest): L'objet de la requête HTTP.
    - username (str): Le nom d'utilisateur du profil à récupérer.

    Returns:

    - HttpResponse: La réponse HTTP avec le contenu HTML de la page de détail du profil
    - le template 404.html en cas d'erreur.
    """
    try:
        profile = get_object_or_404(Profile, user__username=username)
        logger.info(f"Profil trouvé: {profile}")
        context = {"profile": profile}
        return render(request, "profiles/profile.html", context)
    except Exception as e:
        logger.error(
            f"Erreur lors de la récupération du profil pour l'utilisateur {username}: {e}"
        )
        return render(request, "oc_lettings_site/404.html", status=404)
