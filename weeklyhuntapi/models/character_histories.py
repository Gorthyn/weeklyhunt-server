from django.db import models

class CharacterHistory(models.Model):
    character = models.ForeignKey("Character", on_delete=models.CASCADE)
    history = models.ForeignKey("History", on_delete=models.CASCADE)
    characterName = models.CharField(max_length=200)
