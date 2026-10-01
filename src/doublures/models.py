from django.db import models


class Doublure(models.Model):
    """Maps to the `doublure_names` table created by `data/doublure.sql`."""

    firstname = models.CharField(max_length=50)
    name = models.CharField(max_length=50, primary_key=True)

    class Meta:
        managed = False
        db_table = "doublure_names"

    def __str__(self):
        return f"{self.firstname} {self.name}"
