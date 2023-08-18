from django.db import models

class Sect(models.Model):
    tradition = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    