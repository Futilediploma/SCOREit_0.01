from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:league_id>/', views.add_team, name='add_team'),
    path('view/<int:league_id>/', views.view_teams, name='view_teams'),
    path('edit/<int:team_id>/', views.edit_team, name='edit_team'),

    # Add other team-related URLs here, such as team list, edit, or delete
]
