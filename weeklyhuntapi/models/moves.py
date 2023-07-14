from django.db import models

class Move(models.Model):
    playbook = models.ForeignKey("Playbook", on_delete=models.CASCADE)
    isRequired = models.BooleanField()
    name = models.CharField(max_length=200)
    description = models.TextField()
