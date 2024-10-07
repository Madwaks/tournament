from django.db.models import Model, ForeignKey, CASCADE


class Pool(Model):
    tournament = ForeignKey('Tournament', on_delete=CASCADE, related_name='pools')

    teams = ManyToManyField('Team', related_name='pools')