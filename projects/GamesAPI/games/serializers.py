from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ("id", "name", "release_date", "game_category", "played",)

    def is_empty(self, value):
        if value is None or value == "":
            raise serializers.ValidationError("Value shouldn't be empty!")
        return value

    def is_registered(self, value):
        if value in list(map(lambda it: it.name, Game.objects.filter(name=value).exclude(id=self.initial_data['id']))):
            raise serializers.ValidationError("This game is already registered!")

    def validate_name(self, name):
        self.is_registered(name)
        return self.is_empty(value=name)

    def validate_release_date(self, release_date):
        return self.is_empty(value=release_date)

    def validate_game_category(self, game_category):
        return self.is_empty(value=game_category)
