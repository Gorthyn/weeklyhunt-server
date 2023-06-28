from django.db import models

class Gear(models.Model):
    name = models.CharField(max_length=200)
    harm = models.IntegerField()
    playbook = models.ForeignKey("Playbook", on_delete=models.CASCADE)
