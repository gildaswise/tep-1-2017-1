from django.db import models


class GameCategory(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Game(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True)
    release_date = models.DateTimeField()
    game_category = models.ForeignKey(GameCategory, related_name="games")
    played = models.BooleanField(default=False)

    class Meta:
        ordering = ("id", "name",)


class Player(models.Model):

    MALE, FEMALE = "M", "F"
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=False)
    gender = models.CharField(max_length=2,
                              choices=GENDER_CHOICES,
                              default=MALE)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Score(models.Model):

    score = models.IntegerField()
    score_date = models.DateTimeField()
    game = models.ForeignKey(Game, related_name="scores")
    player = models.ForeignKey(Player, related_name="scores")

    class Meta:
        ordering = ("-score",)
