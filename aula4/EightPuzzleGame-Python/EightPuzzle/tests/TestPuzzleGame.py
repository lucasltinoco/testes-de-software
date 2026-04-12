import unittest
from puzzle_game import PuzzleGame
from invalid_position_exception import InvalidPositionException

class TestDataFlowGetTile(unittest.TestCase):
    def setUp(self):
        self.game = PuzzleGame(3) 
        self.game.line_of_empty_position = 2
        self.game.column_of_empty_position = 2

    # Caminho: 1 -> 5
    def test_get_tile_posicao_invalida(self):
        with self.assertRaises(InvalidPositionException):
            self.game.get_tile(0, 1)

    # Caminho: 1 -> 2 -> 3
    def test_get_tile_posicao_vazia(self):
        result = self.game.get_tile(2, 2)
        self.assertEqual(result, " ")

    # Caminho: 1 -> 2 -> 4
    def test_get_tile_posicao_com_peca(self):
        tile_value = self.game.board.get_tile(1, 1)
        result = self.game.get_tile(1, 1)
        
        self.assertEqual(result, tile_value)
        self.assertNotEqual(result, " ")

if __name__ == "__main__":
    unittest.main()