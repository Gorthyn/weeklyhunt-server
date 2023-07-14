from django.db import models

class Improvement(models.Model):
    playbook = models.ForeignKey("Playbook", on_delete=models.CASCADE)
    improvement = models.CharField(max_length=200)
