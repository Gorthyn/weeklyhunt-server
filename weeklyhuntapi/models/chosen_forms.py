from django.db import models

class ChosenForm(models.Model):
    name = models.CharField(max_length=200)
    harm = models.IntegerField()
