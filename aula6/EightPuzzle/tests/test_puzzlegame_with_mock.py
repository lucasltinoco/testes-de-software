import unittest

from unittest.mock import patch, Mock
from puzzle_game_with_mock import PuzzleGameWithPlayer

from shufflers_for_testing_puzzles import TestingShufflerPuzzleGame2x2To1X32, TestingShufflerPuzzleGame3x3To12345X786


class TestWithoutMock(unittest.TestCase):
    def setUp(self):
        self.puzzle_game = PuzzleGameWithPlayer(2, "Lucas")
        TestingShufflerPuzzleGame2x2To1X32().shuffle(self.puzzle_game)
        
    def test_end_of_the_game_with_unfinished_game(self):
        result = self.puzzle_game.end_of_the_game()
        self.assertEqual(result, "Game not finished")
        
    def test_end_of_the_game_with_finished_game_2x2(self):
        self.puzzle_game.board.grid = [[1, 2], [3, None]]
        result = self.puzzle_game.end_of_the_game()
        self.assertEqual(result, "Saved")
            
    def test_end_of_the_game_with_finished_game_3x3(self):
        self.puzzle_game = PuzzleGameWithPlayer(3, "Lucas")
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(self.puzzle_game)
        self.puzzle_game.board.grid = [[1, 2, 3], [4, 5, 6], [7, 8, None]]
        result = self.puzzle_game.end_of_the_game()
        self.assertEqual(result, "Saved")

class TestWithMock(unittest.TestCase):
    def setUp(self):
        self.puzzle_game = PuzzleGameWithPlayer(2, "Lucas")
        TestingShufflerPuzzleGame2x2To1X32().shuffle(self.puzzle_game)
        
    @patch('puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_end_of_the_game_with_unfinished_game(self, mock_save_game_to_file):
        mock_save_game_to_file.return_value = "Saved"
        result = self.puzzle_game.end_of_the_game()
        self.assertEqual(result, "Game not finished")

    @patch('puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_end_of_the_game_with_finished_game_2x2(self, mock_save_game_to_file):
        self.puzzle_game.board.grid = [[1, 2], [3, None]]
        mock_save_game_to_file.return_value = "Saved"
        result = self.puzzle_game.end_of_the_game()
        self.assertEqual(result, "Saved")
        mock_save_game_to_file.assert_called_once()

    @patch('puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_end_of_the_game_with_finished_game_3x3(self, mock_save_game_to_file):
        self.puzzle_game = PuzzleGameWithPlayer(3, "Lucas")
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(self.puzzle_game)
        self.puzzle_game.board.grid = [[1, 2, 3], [4, 5, 6], [7, 8, None]]
        mock_save_game_to_file.return_value = "Saved"
        result = self.puzzle_game.end_of_the_game()
        self.assertEqual(result, "Saved")
        mock_save_game_to_file.assert_called_once()

if __name__ == "__main__":
    unittest.main()
