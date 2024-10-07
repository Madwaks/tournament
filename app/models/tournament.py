from django.db import models
from django.db.models import Model


class Tournament(Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField()

    teams = models.ManyToManyField('Team', related_name='tournaments')

    def __str__(self):
        return self.name

