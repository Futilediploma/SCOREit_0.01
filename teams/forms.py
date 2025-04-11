from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'name', 
            'league',    # Remove this if you plan to set the league in the view
            'division',
            'coach1',
            'coach2', 
            'home_field_name', 
            'home_field_address', 
            'home_field_city', 
            'home_field_zipcode'
        ]
        labels = {
            'name': 'Team Name',
            'league': 'League',
            'division': 'Divison',
            'coach1': 'Coach 1',
            'coach2': 'Coach 2',
            'home_field_name': 'Home Field Name',
            'home_field_address': 'Home Field Address',
            'home_field_city': 'Home Field City',
            'home_field_zipcode': 'Home Field Zipcode',
        }
        # Optionally, you can add widgets or help_texts here.
