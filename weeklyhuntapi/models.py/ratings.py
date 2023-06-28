from django.db import models

class Rating(models.Model):
    playbook = models.ForeignKey("Playbook", on_delete=models.CASCADE)
    charm = models.IntegerField()
    cool = models.IntegerField()
    sharp = models.IntegerField()
    tough = models.IntegerField()
    weird = models.IntegerField()
