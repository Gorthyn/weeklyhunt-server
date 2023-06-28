from django.db import models

class ChosenBusinessEnd(models.Model):
    name = models.CharField(max_length=200)
    harm = models.IntegerField()
