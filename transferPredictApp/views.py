from email.mime import application
from django.shortcuts import render
from django.http import JsonResponse

from .Overview import home_table
from .Players import players_tournament
from .Players import players_players
from .Players import get_player_info
from .Players import radar_plot
from .Players import violin_plot
from .Players import scatter_plot
from .Similarity import similarity_plot
from .Predictions import predictions

def home(request):
    tournament = request.GET["tournament"]
    position = request.GET["position"]
    result = home_table.home_table(tournament, position)
    return JsonResponse(result, safe=False)

def players_tournament_filter(request):
    tournament = request.GET["tournament"]
    result = players_tournament.players_tournament(tournament)
    return JsonResponse(result, safe=False)

def search_players(request):
    tournament = request.GET["tournament"]
    team = request.GET["team"]
    position = request.GET["position"]
    result = players_players.players_players(tournament, team, position)
    return JsonResponse(result, safe=False)

def get_player(request):
    tournament = request.GET["tournament"]
    team = request.GET["team"]
    position = request.GET["position"]
    name = request.GET["name"]
    result = get_player_info.get_player_info(tournament, team, position, name)
    return JsonResponse(result, safe=False)
    
def get_radar_plot(request):
    tournament = request.GET["tournament"]
    team = request.GET["team"]
    position = request.GET["position"]
    name = request.GET["name"]
    result = radar_plot.radar_plot(tournament, team, position, name)
    return JsonResponse(result, safe=False)

def get_violin_plot(request):
    tournament = request.GET["tournament"]
    team = request.GET["team"]
    position = request.GET["position"]
    name = request.GET["name"]
    attributum = request.GET["attributum"]
    result = violin_plot.violin_plot(tournament, team, position, name, attributum)
    return JsonResponse(result, safe=False)

def get_scatter_plot(request):
    tournament = request.GET["tournament"]
    team = request.GET["team"]
    position = request.GET["position"]
    name = request.GET["name"]
    attr1 = request.GET["attr1"]
    attr2 = request.GET["attr2"]
    result = scatter_plot.scatter_plot(tournament, team, position, name, attr1, attr2)
    return JsonResponse(result, safe=False)

def get_similarity_plot(request):
    name = request.GET["name"]
    position = request.GET["position"]
    result = similarity_plot.similarity_plot(position, name)
    return JsonResponse(result, safe=False)

def get_predictions(request):
    tournament = request.GET["tournament"]
    team = request.GET["team"]
    position = request.GET["position"]
    result = predictions.predictions(tournament, team, position)
    return JsonResponse(result, safe=False)