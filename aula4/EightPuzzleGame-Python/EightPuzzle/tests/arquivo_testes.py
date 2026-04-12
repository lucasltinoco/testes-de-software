import unittest

from board import Board
from puzzle_game import PuzzleGame

from shufflers_for_testing_puzzles import TestingShufflerPuzzleGame2x2To1X32

class ClasseTestes(unittest.TestCase):
    def setUp(self):
        self.puzzle_game = PuzzleGame(2)
    
    # Testes comandos 
    def test_one(self):
      TestingShufflerPuzzleGame2x2To1X32().shuffle(self.puzzle_game)

if __name__ == "__main__":
    unittest.main()
