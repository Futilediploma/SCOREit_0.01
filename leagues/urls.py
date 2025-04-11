from django.urls import path
from .views import league_list, add_league, edit_league, delete_league

urlpatterns = [
    path('add/', add_league, name='add_league'),
    path('edit/<int:league_id>/', edit_league, name='edit_league'),
    path('delete/<int:league_id>/', delete_league, name='delete_league'),
    path('', league_list, name='league_list'),
]
