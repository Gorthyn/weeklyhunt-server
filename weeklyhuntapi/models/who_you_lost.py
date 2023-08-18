from django.db import models

class WhoYouLost(models.Model):
    relation = models.CharField(max_length=255)
    