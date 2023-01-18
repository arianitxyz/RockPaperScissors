import unittest
import game


class TestPlay(unittest.TestCase):
    def test_play_manual(self):
        play = game.play('r', 'p', False)
        self.assertEqual(play, 'opponent wins: p > r')


if __name__ == '__main__':
    unittest.main()
