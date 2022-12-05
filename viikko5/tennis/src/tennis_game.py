class TennisGame:
    """Point counter for tennis."""
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score_names = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

    def won_point(self, player_name):
        """Give a point to one of the players."""
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1
        else:
            pass

    def _even_score_reading(self) -> str:
        """Get score reading for even scores."""
        if self.player1_score >= 4:
            return "Deuce"
        return f"{self.score_names[self.player1_score]}-All"

    def _player_in_lead(self) -> str:
        """Get the name of the player with higher points.

        If scores are same, returns empty string.
        """
        if self.player1_score > self.player2_score:
            return self.player1_name
        elif self.player1_score < self.player2_score:
            return self.player2_name
        else:
            return ''

    def _uneven_score_set_point_reading(self) -> str:
        """Get score reading for set points when set is not even."""
        point_diff = abs(self.player1_score - self.player2_score)
        if point_diff == 1:
            return f"Advantage {self._player_in_lead()}"
        return f"Win for {self._player_in_lead()}"

    def _uneven_score_reading(self) -> str:
        """Get score reading for points where set score is not even."""
        return (f"{self.score_names[self.player1_score]}-"
                f"{self.score_names[self.player2_score]}")

    def get_score(self) -> str:
        """Get score reading of the game."""
        if self.player1_score == self.player2_score:
            return self._even_score_reading()
        elif max(self.player1_score, self.player2_score) >= 4:
            return self._uneven_score_set_point_reading()
        return self._uneven_score_reading()
