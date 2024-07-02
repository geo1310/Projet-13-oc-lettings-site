from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView

from . import views


handler404 = "oc_lettings_site.views.custom_handler404"
handler500 = "oc_lettings_site.views.custom_handler500"

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path("404/", TemplateView.as_view(template_name="oc_lettings_site/404.html"), name="404"),
        path("500/", TemplateView.as_view(template_name="oc_lettings_site/500.html"), name="500"),
    ]
