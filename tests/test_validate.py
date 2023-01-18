import unittest
import game


class TestValidate(unittest.TestCase):

    def test_validate_tie(self):
        tie_game = game.validate('r', 'r')
        self.assertEqual(tie_game, 'nobody wins r = r')

        tie_game = game.validate('p', 'p')
        self.assertEqual(tie_game, 'nobody wins p = p')

        tie_game = game.validate('s', 's')
        self.assertEqual(tie_game, 'nobody wins s = s')

    def test_validate_opponent_wins(self):
        opponent_wins = game.validate('s', 'r')
        self.assertEqual(opponent_wins, 'opponent wins: r > s')

        opponent_wins = game.validate('r', 'p')
        self.assertEqual(opponent_wins, 'opponent wins: p > r')

        opponent_wins = game.validate('p', 's')
        self.assertEqual(opponent_wins, 'opponent wins: s > p')

    def test_validate_player_wins(self):
        player_wins = game.validate('r', 's')
        self.assertEqual(player_wins, 'player wins: r > s')

        player_wins = game.validate('p', 'r')
        self.assertEqual(player_wins, 'player wins: p > r')

        player_wins = game.validate('s', 'p')
        self.assertEqual(player_wins, 'player wins: s > p')


if __name__ == '__main__':
    unittest.main()
