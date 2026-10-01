from django.db import models


class PremierRole(models.Model):
    """Maps to the `role_names` table created by `data/premier_roles.sql`."""

    firstname = models.CharField(max_length=50)
    name = models.CharField(max_length=50, primary_key=True)

    class Meta:
        managed = False
        db_table = "role_names"

    def __str__(self):
        return f"{self.firstname} {self.name}"
