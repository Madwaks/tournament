from random import sample

from app.models import Tournament, Team
from itertools import islice

def chunk_list(team_list: list[Team], max_elems: int):
    it = iter(sample(team_list, len(team_list)))
    return [list(islice(it, max_elems)) for _ in range(0, len(team_list), max_elems)]

class TournamentService:
    def create_tournament_pools(self, tournament: Tournament):
        teams = tournament.teams.all()
        # Implement your logic here

        return teams

