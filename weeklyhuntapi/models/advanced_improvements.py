from django.db import models

class AdvancedImprovements(models.Model):
    playbook = models.ForeignKey('Playbook', on_delete=models.CASCADE)
    description = models.TextField()
    