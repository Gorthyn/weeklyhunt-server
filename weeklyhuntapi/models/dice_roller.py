from django.db import models

class DiceRoll(models.Model):
    result_1 = models.PositiveIntegerField()
    result_2 = models.PositiveIntegerField()
    modifier = models.IntegerField()
    total = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Roll: {self.result_1} + {self.result_2} + {self.modifier} = {self.total}'
