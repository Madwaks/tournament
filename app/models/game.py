from django.db.models import Model, CASCADE, ForeignKey, IntegerField, DateTimeField


class Game(Model):
    tournament = ForeignKey('Tournament', on_delete=CASCADE)
    home_team = ForeignKey('Team', on_delete=CASCADE, related_name='home_games')
    away_team = ForeignKey('Team', on_delete=CASCADE, related_name='away_games')

    score_home = IntegerField(null=True)
    score_away = IntegerField(null=True)

    date_time = DateTimeField(null=True)

    def __str__(self):
        return f'{self.home_team} vs {self.away_team} - {self.score_home or "-"} : {self.score_away or "-"}'