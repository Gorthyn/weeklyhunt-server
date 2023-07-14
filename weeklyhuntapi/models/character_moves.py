from django.db import models

class CharacterMove(models.Model):
    move = models.ForeignKey("Move", on_delete=models.CASCADE)
    character = models.ForeignKey("Character", on_delete=models.CASCADE)
