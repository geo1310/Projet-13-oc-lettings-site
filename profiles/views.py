from django.shortcuts import render
from .models import Profile


def index(request):
    """
    Fonction de vue pour la page d'accueil de l'application des profils.

    Récupère tous les profils de la base de données et rend le template index.

    Args:
        request: L'objet de la requête HTTP.

    Returns:
        HttpResponse: HTML rendu de la page d'accueil avec la liste des profils.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Fonction de vue pour la page de détail d'un profil.

    Récupère le profil par le nom d'utilisateur et rend le template du profil avec ses détails.

    Args:
        request: L'objet de la requête HTTP.
        username: Le nom d'utilisateur du profil à récupérer.

    Returns:
        HttpResponse: HTML rendu de la page de détail du profil avec les informations du profil.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
