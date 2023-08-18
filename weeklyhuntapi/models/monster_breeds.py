from django.db import models

class MonsterBreeds(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    