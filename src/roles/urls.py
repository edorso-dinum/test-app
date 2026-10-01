from django.urls import path

from . import views

urlpatterns = [
    path("", views.premier_role_list, name="premier-role-list"),
]
