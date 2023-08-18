from django.db import models

class Look(models.Model):
    playbook = models.ForeignKey('Playbook', on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    