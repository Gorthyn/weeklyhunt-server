from django.db import models

class ChosenMaterial(models.Model):
    name = models.CharField(max_length=200)
