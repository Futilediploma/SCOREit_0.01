from django.db import models
from leagues.models import League  # Import the League model

class Team(models.Model):
    name = models.CharField(max_length=100)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="teams")
    division = models.CharField(max_length=50)
    coach1 = models.CharField(max_length=100)
    coach2 = models.CharField(max_length=100)
    home_field_name = models.CharField(max_length=100)
    home_field_address = models.CharField(max_length=500)
    home_field_city = models.CharField(max_length=100)
    home_field_zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.name
