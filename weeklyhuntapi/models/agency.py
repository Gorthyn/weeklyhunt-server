from django.db import models

class Agency(models.Model):
    type = models.CharField(max_length=255)
    