import unittest
from statistics import Statistics, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_nonexistent_player(self):
        player = self.statistics.search("Matti")
        self.assertIs(player, None)

    def test_search_existing_player(self):
        player = self.statistics.search("Semenko")
        self.assertEqual(
            player.name,
            "Semenko"
        )

    def test_team(self):
        players = self.statistics.team("PIT")
        self.assertEqual(
            players[0].name,
            "Lemieux"
        )

    def test_top1_noargs(self):
        result = self.statistics.top(1)
        self.assertEqual(
            "Gretzky",
            result[0].name
        )

    def test_top1_points(self):
        result = self.statistics.top(1, SortBy.POINTS)
        self.assertEqual(
            "Gretzky",
            result[0].name
        )

    def test_top1_assists(self):
        result = self.statistics.top(1, SortBy.ASSISTS)
        self.assertEqual(
            "Gretzky",
            result[0].name
        )

    def test_top1_goals(self):
        result = self.statistics.top(1, SortBy.GOALS)
        self.assertEqual(
            "Lemieux",
            result[0].name
        )
