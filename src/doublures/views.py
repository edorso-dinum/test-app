from django.shortcuts import render

from .models import Doublure


def doublure_list(request):
    doublures = Doublure.objects.all().order_by("firstname", "name")
    return render(request, "doublures/list.html", {"doublures": doublures})
