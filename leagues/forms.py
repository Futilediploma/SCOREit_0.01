from django import forms
from .models import League

class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ['name', 'season', 'session', 'year', 'sex', 'age', 'divisions', 'notes']
        labels = {
            'name': 'League Name',
            'season': 'Season',
            'session': 'Session',
            'year': 'Season Year',
            'sex': 'Gender',
            'age': 'Age Group',
            'divisions': 'Number of Divisions',
            'notes': 'Supplemental Notes',
        }
        help_texts = {
            'year': 'Enter the 4-digit year for this league (e.g., 2025)',
        }