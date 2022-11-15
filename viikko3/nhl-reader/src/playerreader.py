"""Module with PlayerReader class."""
import requests
from player import Player


class PlayerReader:
    """Object for reading and keeping a list of players."""
    def __init__(self, url):
        self.url = url

    def get_players(self):
        """Get a list of Player-objects."""
        data = requests.get(self.url).json()
        return [Player(player_dict) for player_dict in data]
