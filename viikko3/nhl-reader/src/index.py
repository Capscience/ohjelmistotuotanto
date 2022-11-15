"""File for running example code."""
from datetime import datetime
import requests
from player import Player


def main():
    """Run example code for project."""
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        if player_dict['nationality'] != 'FIN':
            continue
        player = Player(player_dict)

        players.append(player)

    print(f'Player from FIN {datetime.now()}\n')

    for player in sorted(players, reverse=True):
        print(player)


if __name__ == "__main__":
    main()
