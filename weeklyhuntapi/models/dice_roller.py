from django.db import models

class DiceRoll(models.Model):
    result_1 = models.PositiveIntegerField()
    result_2 = models.PositiveIntegerField()
    modifier = models.IntegerField(default=0)
    total = models.IntegerField()
    roll_type = models.CharField(max_length=50)

    def __str__(self):
        return f'Roll: {self.result_1} + {self.result_2} + {self.modifier} = {self.total}'
