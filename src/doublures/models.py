from django.db import models


class Doublure(models.Model):
    """Stores the `doublure_names` table, created and seeded by Django migrations."""

    firstname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "doublure_names"

    def __str__(self):
        return f"{self.firstname} {self.name}"
