from django.db.models import Model, CharField, ManyToManyField, ForeignKey, CASCADE


class Team(Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name
