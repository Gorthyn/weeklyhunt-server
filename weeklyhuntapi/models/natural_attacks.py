from django.db import models

class NaturalAttacks(models.Model):
    name = models.CharField(max_length=255)
    harm = models.PositiveIntegerField()
    range = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    