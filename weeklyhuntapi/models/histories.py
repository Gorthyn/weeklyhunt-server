from django.db import models

class History(models.Model):
    playbook = models.ForeignKey("Playbook", on_delete=models.CASCADE)
    description = models.TextField()
