import unittest
from src import game

class TestGame(unittest.TestCase):
    def test_determine_winner(self):
        self.assertEqual(game.determine_winner('rock', 'scissors'), 'rock')
        self.assertEqual(game.determine_winner('rock', 'paper'), 'paper')
        self.assertEqual(game.determine_winner('rock', 'rock'), 'draw')
        self.assertEqual(game.determine_winner('paper', 'scissors'), 'scissors')
        self.assertEqual(game.determine_winner('paper', 'rock'), 'paper')
        self.assertEqual(game.determine_winner('paper', 'paper'), 'draw')
        self.assertEqual(game.determine_winner('scissors', 'rock'), 'rock')
        self.assertEqual(game.determine_winner('scissors', 'paper'), 'scissors')
        self.assertEqual(game.determine_winner('scissors', 'scissors'), 'draw')

if __name__ == '__main__':
    unittest.main()