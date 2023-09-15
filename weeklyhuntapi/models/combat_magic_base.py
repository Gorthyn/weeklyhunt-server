from django.db import models

class CombatMagicBase(models.Model):
    name = models.CharField(max_length=255)
    harm = models.IntegerField()
    type = models.CharField(max_length=50)
    range = models.CharField(max_length=50)
    attributes = models.JSONField()
    