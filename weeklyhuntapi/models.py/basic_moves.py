from django.db import models

class BasicMove(models.Model):
    name = models.CharField(max_length=200)
