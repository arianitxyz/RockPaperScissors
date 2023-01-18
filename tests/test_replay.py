import random
import unittest
import game


class TestReplay(unittest.TestCase):
    def test_replay_true(self):
        true = game.replay('yes')
        self.assertEqual(true, True)

    def test_replay_error(self):
        error = game.replay('test')
        self.assertEqual(error, False)

    def test_replay_false(self):
        false = game.replay('no')
        self.assertEqual(false, False)


if __name__ == '__main__':
    unittest.main()
