from django.db import models
from django.contrib.auth.models import User

class League(models.Model):
    name = models.CharField(max_length=100)
    season = models.CharField(max_length=20, default='')  # e.g., "fall", "spring"
    session = models.CharField(max_length=20, default='')  # Only needed if you have a separate concept
    year = models.PositiveIntegerField()
    sex = models.CharField(max_length=10, default='')  # e.g., "Co-ed", "Boys", "Girls"
    age = models.CharField(max_length=10, null=True, blank=True)
    divisions = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)  # New field
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leagues')
    created_at = models.DateTimeField(auto_now_add=True)  # New field to record creation time

    def __str__(self):
        return f"{self.name} - {self.year}"
