from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('overview/', views.home, name = 'home'),
    path('tournament/', views.players_tournament_filter, name = 'players_tournament'),
    path('players/', views.search_players, name = 'search_players'),
    path('playerinfo/', views.get_player, name = 'get_player'),
    path('radarplot/', views.get_radar_plot, name = 'radarplot'),
    path('violinplot/', views.get_violin_plot, name = 'violinplot'),
    path('scatterplot/', views.get_scatter_plot, name = 'scatterplot'),
    path('similarity_plot/', views.get_similarity_plot, name = 'similarity_plot'),
    path('predictions/', views.get_predictions, name = 'predictions')
]