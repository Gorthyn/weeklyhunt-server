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
    # Sections belonging to all playbooks
    advanced_improvements = models.ManyToManyField('AdvancedImprovements', blank=True)
    basic_moves = models.ManyToManyField('BasicMoves', blank=True)
    histories = models.ManyToManyField('Histories', blank=True)
    improvements = models.ManyToManyField('Improvements', blank=True)
    look = models.ManyToManyField('Look', blank=True)
    moves = models.ManyToManyField('Moves', blank=True)
    ratings = models.ManyToManyField('Ratings', blank=True)
    gear = models.ManyToManyField('Gear', blank=True)
    dice_roller = models.ManyToManyField('DiceRoller', blank=True)