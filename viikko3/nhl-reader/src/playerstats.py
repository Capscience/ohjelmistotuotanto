"""Module with PlayerStatistics class."""


class PlayerStats:
    """Class for statistics of NHL players."""
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality) -> list:
        """Get list of players ordered by points."""
        players = [player for player in self.reader.get_players()
                   if player.nationality == nationality]
        return sorted(players, reverse=True)
