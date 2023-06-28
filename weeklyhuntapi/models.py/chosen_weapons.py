from django.db import models

class ChosenWeapon(models.Model):
    character = models.ForeignKey("Character", on_delete=models.CASCADE)
    form = models.ForeignKey("ChosenForm", on_delete=models.CASCADE)
    formHarm = models.IntegerField()
    material = models.ForeignKey("ChosenMaterial", on_delete=models.CASCADE)
    businessEnd1 = models.ForeignKey("ChosenBusinessEnd", on_delete=models.CASCADE, related_name='weapon_businessEnd1')
    businessEndHarm1 = models.IntegerField()
    businessEnd2 = models.ForeignKey("ChosenBusinessEnd", on_delete=models.CASCADE, related_name='weapon_businessEnd2')
    businessEndHarm2 = models.IntegerField()
    businessEnd3 = models.ForeignKey("ChosenBusinessEnd", on_delete=models.CASCADE, related_name='weapon_businessEnd3')
    businessEndHarm3 = models.IntegerField()
