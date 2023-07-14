from django.db import models

class CharacterGear(models.Model):
    character = models.ForeignKey("Character", on_delete=models.CASCADE)
    gear = models.ForeignKey("Gear", on_delete=models.CASCADE)
