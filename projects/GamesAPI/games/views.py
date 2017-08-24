"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""

from datetime import datetime

from django.urls import reverse
from django.utils import timezone
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import *
from .serializers import *


class GameCategoryList(generics.ListCreateAPIView):

    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = "gamecategory-list"


class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = "gamecategory-detail"


class GameList(generics.ListCreateAPIView):

    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = "game-list"


class GameDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = "game-detail"


class PlayerList(generics.ListCreateAPIView):

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = "player-list"


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = "player-detail"


class ScoreList(generics.ListCreateAPIView):

    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    name = "score-list"


class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    name = "score-detail"


class ApiRoot(generics.GenericAPIView):

    name = "root"

    def get(self, request, *args, **kwargs):
        return Response({
            "players": reverse(PlayerList.name),
            "categories": reverse(GameCategoryList.name),
            "games": reverse(GameList.name),
            "scores": reverse(ScoreList.name)
        })


@api_view(["GET", "POST"])
def game_list(request):
    if request.method == "GET":
        games = Game.objects.all()
        games_serializer = GameSerializer(games, many=True)
        return Response(games_serializer.data)
    elif request.method == "POST":
        game_serializer = GameSerializer(data=request.data)
        if game_serializer.is_valid():
            game_serializer.save()
            return Response(game_serializer.data, status=status.HTTP_201_CREATED)
        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def game_detail(request, pk):
    game = get_object_or_404(Game, id=pk)

    if request.method == "GET":
        game_serializer = GameSerializer(game)
        return Response(game_serializer.data)
    elif request.method == "PUT":
        game_serializer = GameSerializer(game, data=request.data)
        if game_serializer.is_valid():
            game_serializer.save()
            return Response(game_serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        today = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
        if today < game.release_date:
            game.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"release_date": "This game is already launched!"}, status=status.HTTP_403_FORBIDDEN)
