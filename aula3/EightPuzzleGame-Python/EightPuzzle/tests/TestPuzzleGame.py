import unittest

from puzzle_game import PuzzleGame

from shufflers_for_testing_puzzles import TestingShufflerPuzzleGame2x2To1X32


class TestCommandCoverage(unittest.TestCase):
    def setUp(self):
        self.puzzle_game = PuzzleGame(2)
        TestingShufflerPuzzleGame2x2To1X32().shuffle(self.puzzle_game)

    # 1 -> 2 -> 3 (T) -> 5 -> 6 -> 7
    def test_mover_tile_para_posicao_vazia(self):
        result = self.puzzle_game.move_tile(1)
        self.assertEqual(self.puzzle_game.board.get_tile(1, 1), None)
        self.assertEqual(self.puzzle_game.board.get_tile(1, 2), 1)
        self.assertEqual(self.puzzle_game.board.get_tile(2, 1), 3)
        self.assertEqual(self.puzzle_game.board.get_tile(2, 2), 2)
        self.assertTrue(result)

    # 1 -> 2 -> 3 (F) -> 4
    def test_mover_tile_de_fora_do_tabuleiro(self):
        self.puzzle_game.dic_positions_of_tiles.update({4: (3, 3)})
        result = self.puzzle_game.move_tile(4)
        self.assertEqual(self.puzzle_game.board.get_tile(1, 1), 1)
        self.assertEqual(self.puzzle_game.board.get_tile(1, 2), None)
        self.assertEqual(self.puzzle_game.board.get_tile(2, 1), 3)
        self.assertEqual(self.puzzle_game.board.get_tile(2, 2), 2)
        self.assertFalse(result)


class TestBranchCoverage(unittest.TestCase):
    def setUp(self):
        self.puzzle_game = PuzzleGame(2)
        TestingShufflerPuzzleGame2x2To1X32().shuffle(self.puzzle_game)

    # 1 -> 2 -> 3 (T) -> 5 (T) -> 6 -> 7 
    def test_mover_tile_para_posicao_vazia(self):
        result = self.puzzle_game.move_tile(1)
        self.assertEqual(self.puzzle_game.board.get_tile(1, 1), None)
        self.assertEqual(self.puzzle_game.board.get_tile(1, 2), 1)
        self.assertEqual(self.puzzle_game.board.get_tile(2, 1), 3)
        self.assertEqual(self.puzzle_game.board.get_tile(2, 2), 2)
        self.assertTrue(result)

    # 1 -> 2 -> 3 (F) -> 4
    def test_mover_tile_de_fora_do_tabuleiro(self):
        self.puzzle_game.dic_positions_of_tiles.update({4: (3, 3)})
        result = self.puzzle_game.move_tile(4)
        self.assertEqual(self.puzzle_game.board.get_tile(1, 1), 1)
        self.assertEqual(self.puzzle_game.board.get_tile(1, 2), None)
        self.assertEqual(self.puzzle_game.board.get_tile(2, 1), 3)
        self.assertEqual(self.puzzle_game.board.get_tile(2, 2), 2)
        self.assertFalse(result)

    # 1 -> 2 -> 3 (T) -> 5 (F) -> 4
    def test_mover_tile_para_posicao_vazia_2(self):
        result = self.puzzle_game.move_tile(3)
        self.assertEqual(self.puzzle_game.board.get_tile(1, 1), 1)
        self.assertEqual(self.puzzle_game.board.get_tile(1, 2), None)
        self.assertEqual(self.puzzle_game.board.get_tile(2, 1), 3)
        self.assertEqual(self.puzzle_game.board.get_tile(2, 2), 2)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
