from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    playbook = models.ForeignKey("Playbook", on_delete=models.CASCADE)
    rating = models.ForeignKey("Rating", on_delete=models.CASCADE)
    harm_slots = models.IntegerField()
    luck_slots = models.IntegerField()
    experience_slots = models.IntegerField()
    description = models.TextField()
