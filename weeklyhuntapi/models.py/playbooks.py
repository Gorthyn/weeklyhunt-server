from django.db import models

class Playbook(models.Model):
    name = models.CharField(max_length=200)
    luck_special = models.TextField()
    required_move_slots = models.IntegerField()
    optional_move_slots = models.IntegerField()
    total_move_slots = models.IntegerField()
    gear_slots = models.IntegerField()
    luck_slots = models.IntegerField()
    harm_slots = models.IntegerField()
    experience_slots = models.IntegerField()
    description = models.TextField()
