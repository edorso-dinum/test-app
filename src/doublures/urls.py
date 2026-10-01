from django.urls import path

from . import views

urlpatterns = [
    path("", views.doublure_list, name="doublure-list"),
]
