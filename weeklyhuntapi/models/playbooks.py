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
    # Sections belonging to specific playbooks
    agency_goals = models.ForeignKey('AgencyGoals', on_delete=models.SET_NULL, null=True, blank=True)
    agency = models.ForeignKey('Agency', on_delete=models.SET_NULL, null=True, blank=True)
    background = models.ForeignKey('Background', on_delete=models.SET_NULL, null=True, blank=True)
    chosen_business_ends = models.ForeignKey('ChosenBusinessEnd', on_delete=models.SET_NULL, null=True, blank=True)
    chosen_forms = models.ForeignKey('ChosenForms', on_delete=models.SET_NULL, null=True, blank=True)
    chosen_materials = models.ForeignKey('ChosenMaterials', on_delete=models.SET_NULL, null=True, blank=True)
    chosen_weapons = models.ForeignKey('ChosenWeapons', on_delete=models.SET_NULL, null=True, blank=True)
    combat_effects = models.ForeignKey('CombatEffect', on_delete=models.SET_NULL, null=True, blank=True)
    combat_magic_effects = models.ForeignKey('CombatMagicBase', on_delete=models.SET_NULL, null=True, blank=True)
    curses = models.ForeignKey('Curse', on_delete=models.SET_NULL, null=True, blank=True)
    dark_side = models.ForeignKey('DarkSide', on_delete=models.SET_NULL, null=True, blank=True)
    doom = models.ForeignKey('Doom', on_delete=models.SET_NULL, null=True, blank=True)
    fate = models.ForeignKey('Fate', on_delete=models.SET_NULL, null=True, blank=True)
    haven = models.ForeignKey('Haven', on_delete=models.SET_NULL, null=True, blank=True)
    heat = models.ForeignKey('Heat', on_delete=models.SET_NULL, null=True, blank=True)
    heroic = models.ForeignKey('Heroic', on_delete=models.SET_NULL, null=True, blank=True)
    mission = models.ForeignKey('Mission', on_delete=models.SET_NULL, null=True, blank=True)
    monster_breeds = models.ForeignKey('MonsterBreeds', on_delete=models.SET_NULL, null=True, blank=True)
    natural_attacks = models.ForeignKey('NaturalAttacks', on_delete=models.SET_NULL, null=True, blank=True)
    reason = models.ForeignKey('Reason', on_delete=models.SET_NULL, null=True, blank=True)
    red_tape = models.ForeignKey('RedTape', on_delete=models.SET_NULL, null=True, blank=True)
    resources = models.ForeignKey('Resources', on_delete=models.SET_NULL, null=True, blank=True)
    sect = models.ForeignKey('Sect', on_delete=models.SET_NULL, null=True, blank=True)
    underworld = models.ForeignKey('Underworld', on_delete=models.SET_NULL, null=True, blank=True)
    who_you_lost = models.ForeignKey('WhoYouLost', on_delete=models.SET_NULL, null=True, blank=True)