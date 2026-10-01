from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("premier-roles/", include("roles.urls")),
    path("doublures/", include("doublures.urls")),
]
