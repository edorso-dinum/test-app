from django.shortcuts import render

from .models import PremierRole


def premier_role_list(request):
    premier_roles = PremierRole.objects.all().order_by("firstname", "name")
    return render(request, "roles/list.html", {"premier_roles": premier_roles})
