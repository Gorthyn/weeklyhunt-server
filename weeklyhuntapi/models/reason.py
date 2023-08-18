from django.db import models

class Reason(models.Model):
    description = models.TextField()
    