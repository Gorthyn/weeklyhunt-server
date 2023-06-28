from django.db import models

class CharacterImprovement(models.Model):
    character = models.ForeignKey("Character", on_delete=models.CASCADE)
    improvement = models.ForeignKey("Improvement", on_delete=models.CASCADE)
