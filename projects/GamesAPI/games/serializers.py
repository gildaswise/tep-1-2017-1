from rest_framework import serializers
from .models import Game, GameCategory, Score, Player


class GameSerializer(serializers.HyperlinkedModelSerializer):

    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(), slug_field="name")

    class Meta:
        model = Game
        fields = ("id", "url", "name", "release_date", "game_category", "played",)

    def is_empty(self, value):
        if value is None or value == "":
            raise serializers.ValidationError("Value shouldn't be empty!")
        return value

    def is_registered(self, value):
        if value in list(map(lambda it: it.name, Game.objects.filter(name=value).exclude(id=self.initial_data["id"]))):
            raise serializers.ValidationError("This game is already registered!")

    def validate_name(self, name):
        self.is_registered(name)
        return self.is_empty(value=name)

    def validate_release_date(self, release_date):
        return self.is_empty(value=release_date)

    def validate_game_category(self, game_category):
        return self.is_empty(value=game_category)


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GameCategory
        fields = ("url", "id", "name", "games",)


class ScoreSerializer(serializers.HyperlinkedModelSerializer):

    game = serializers.SlugRelatedField(queryset=Game.objects.all(),
                                        slug_field="name")
    player = serializers.SlugRelatedField(queryset=Player.objects.all(),
                                          slug_field="name")

    class Meta:
        model = Score
        fields = ("url", "id", "score", "score_date", "player", "game",)


class PlayerSerializer(serializers.HyperlinkedModelSerializer):

    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ("url", "name", "gender", "scores",)
