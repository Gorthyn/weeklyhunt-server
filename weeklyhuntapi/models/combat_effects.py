from django.db import models

class CombatEffect(models.Model):
    name = models.CharField(max_length=255)
    harm_bonus = models.IntegerField()
    type_bonus = models.CharField(max_length=50)
    attributes = models.JSONField()
    special = models.TextField()
    