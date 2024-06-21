from django.db import models
from django.contrib.auth.models import User
from .game_model import Game

class Rating(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()