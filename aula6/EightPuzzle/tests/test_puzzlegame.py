import unittest

from unittest.mock import patch, Mock
from puzzle_game import PuzzleGame

from shufflers_for_testing_puzzles import TestingShufflerPuzzleGame2x2To1X32, TestingShufflerPuzzleGame3x3To12345X786


class TestWithoutMock(unittest.TestCase):
    def setUp(self):
        self.puzzle_game = PuzzleGame(2)
        TestingShufflerPuzzleGame2x2To1X32().shuffle(self.puzzle_game)

    def test_mover_tile_para_posicao_vazia(self):
        result = self.puzzle_game.move_tile(1)
        self.assertEqual(self.puzzle_game.get_tile(1, 1), ' ')
        self.assertEqual(self.puzzle_game.get_tile(1, 2), 1)
        self.assertEqual(self.puzzle_game.get_tile(2, 1), 3)
        self.assertEqual(self.puzzle_game.get_tile(2, 2), 2)
        self.assertTrue(result)

    def test_mover_tile_de_fora_do_tabuleiro(self):
        self.puzzle_game.dic_positions_of_tiles.update({4: (3, 3)})
        result = self.puzzle_game.move_tile(4)
        self.assertEqual(self.puzzle_game.get_tile(1, 1), 1)
        self.assertEqual(self.puzzle_game.get_tile(1, 2), ' ')
        self.assertEqual(self.puzzle_game.get_tile(2, 1), 3)
        self.assertEqual(self.puzzle_game.get_tile(2, 2), 2)
        self.assertFalse(result)
        

class TestWithMock(unittest.TestCase):
    def setUp(self):
        self.puzzle_game = PuzzleGame(2)
        TestingShufflerPuzzleGame2x2To1X32().shuffle(self.puzzle_game)

    @patch('puzzle_game.PuzzleGame.get_tile')
    def test_mover_tile_para_posicao_vazia(self, mock_puzzle_board_get_tile):
        result = self.puzzle_game.move_tile(1)
        mock_puzzle_board_get_tile.return_value = ' '
        self.assertEqual(self.puzzle_game.get_tile(1, 1), ' ')
        mock_puzzle_board_get_tile.return_value = 1
        self.assertEqual(self.puzzle_game.get_tile(1, 2), 1)
        mock_puzzle_board_get_tile.return_value = 3
        self.assertEqual(self.puzzle_game.get_tile(2, 1), 3)
        mock_puzzle_board_get_tile.return_value = 2
        self.assertEqual(self.puzzle_game.get_tile(2, 2), 2)
        self.assertTrue(result)

    @patch('puzzle_game.PuzzleGame.get_tile')
    def test_mover_tile_de_fora_do_tabuleiro(self, mock_puzzle_board_get_tile):
        self.puzzle_game.dic_positions_of_tiles.update({4: (3, 3)})
        result = self.puzzle_game.move_tile(4)
        mock_puzzle_board_get_tile.return_value = 1
        self.assertEqual(self.puzzle_game.get_tile(1, 1), 1)
        mock_puzzle_board_get_tile.return_value = ' '
        self.assertEqual(self.puzzle_game.get_tile(1, 2), ' ')
        mock_puzzle_board_get_tile.return_value = 3
        self.assertEqual(self.puzzle_game.get_tile(2, 1), 3)
        mock_puzzle_board_get_tile.return_value = 2
        self.assertEqual(self.puzzle_game.get_tile(2, 2), 2)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
