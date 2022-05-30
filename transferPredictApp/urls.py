from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    url('overview/', views.home, name = 'home'),
    url('tournament/', views.players_tournament_filter, name = 'players_tournament'),
    url('players/', views.search_players, name = 'search_players'),
    url('playerinfo/', views.get_player, name = 'get_player'),
    url('radarplot/', views.get_radar_plot, name = 'radarplot'),
    url('violinplot/', views.get_violin_plot, name = 'violinplot'),
    url('scatterplot/', views.get_scatter_plot, name = 'scatterplot'),
    # url('similarity/', views.get_similarity, name = 'similarity'),
    url('similarity_plot', views.get_similarity_plot, name = 'similarity_plot'),
    url('predictions/', views.get_predictions, name = 'predictions')
]