import unittest
import game


class TestValidateGame(unittest.TestCase):
    def test_validate_game_tie(self):
        comp_choice = 'r'
        player_choice = 'r'
        self.assertEqual(self.validate_game(comp_choice, player_choice), "Tie since both players chose r")

    def test_validate_game_computer_wins(self):
        comp_choice = 'r'
        player_choice = 's'
        self.assertEqual(self.validate_game(comp_choice, player_choice),
                         "Computer wins! Computer chose r, Player chose s")

    def test_validate_game_player_wins(self):
        comp_choice = 's'
        player_choice = 'p'
