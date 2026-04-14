import unittest

import unittest
from puzzle_game import PuzzleGame
from invalid_position_exception import InvalidPositionException

from shufflers_for_testing_puzzles import TestingShufflerPuzzleGame2x2To1X32, TestingShufflerPuzzleGame3x3To12345X786


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

class TestMutants(unittest.TestCase):
    def setUp(self):
        pass

    # Kills puzzle_game.xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_3: survived
    # and puzzle_game.xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_12: survived
    # Porque gera lista fixa e testa a lista de 3 valores. Qualquer coisa fora não passa
    def test_generate_list_of_tiles(self):
        puzzle_game = PuzzleGame(2)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(puzzle_game)
        list_of_tiles = puzzle_game.__generate_list_of_tiles__()   
        self.assertEqual(list_of_tiles, [1, 2, 3])
        
    # # Kills puzzle_game.xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_20: survived
    # # Testa execução de put_tiles in_dic_positions e dicionario gerado. Como a mutação
    # # despreza o self.dimension do range, outro dicionário é criado
    def test_put_tiles_in_dic_positions(self):
        puzzle_game = PuzzleGame(3)
        puzzle_game.__put_tiles_in_dic_positions__([1, 2, 3, 4, 5, 6, 7, 8])
        dic_positions_of_tiles = puzzle_game.dic_positions_of_tiles
        # {1: (1, 1), 2: (1, 2), 3: (1, 3), 4: (2, 1), 5: (2, 2), 6: (2, 3), 7: (3, 1), 8: (3, 2)}
        self.assertEqual(dic_positions_of_tiles.get(1), (1, 1))
        self.assertEqual(dic_positions_of_tiles.get(2), (1, 2))
        self.assertEqual(dic_positions_of_tiles.get(3), (1, 3))
        self.assertEqual(dic_positions_of_tiles.get(4), (2, 1))
        self.assertEqual(dic_positions_of_tiles.get(5), (2, 2))
        self.assertEqual(dic_positions_of_tiles.get(6), (2, 3))
        self.assertEqual(dic_positions_of_tiles.get(7), (3, 1))
        self.assertEqual(dic_positions_of_tiles.get(8), (3, 2))
        
    # # Kills puzzle_game.xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_33: survived
    # # Faz o shuffle e testa a movimentação pra posição vazia. Como a movimentação é bem sucedida,
    # # deveria retornar True e não False como na mutação
    def test_move_tile_from_a_position_to_the_empty_position_return_true(self):
        puzzle_game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(puzzle_game)
        # 1  2  3
        # 4  5  -
        # 7  8  6
        # print(puzzle_game.board)
        result = puzzle_game.move_tile_from_a_position_to_the_empty_position(2, 2)
        # print(puzzle_game.board)
        # (1,1):1   (1,2):2   (1,3):3   
        # (2,1):4   (2,2):None   (2,3):5   
        # (3,1):7   (3,2):8   (3,3):6
        self.assertTrue(result)
    
    # # Kills puzzle_game.xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_1: survived
    # # and puzzle_game.xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_34: survived
    # # Tenta mover um valor que não é adjacente à célula vazia, mas está dentro do tabuleiro.
    # # Dessa forma, aborda a mutação do if e do retorno booleano
    def test_move_tile_from_a_position_to_the_empty_position_return_false(self):
        puzzle_game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(puzzle_game)
        # 1  2  3
        # 4  5  -
        # 7  8  6
        result = puzzle_game.move_tile_from_a_position_to_the_empty_position(1, 1)
        self.assertFalse(result)

    # # Kills puzzle_game.xǁPuzzleGameǁget_tile__mutmut_6: survived
    # # and puzzle_game.xǁPuzzleGameǁget_tile__mutmut_10: survived
    # # Testa o limite da linha do if inicial e acaba testando a condição da segunda mutação,
    # # Pois a linha 3 bate com linha vazia
    def test_get_tile_with_line_eq_to_limit(self):
        puzzle_game = PuzzleGame(3)
        # print(puzzle_game.board)
         # 1  2  3
         # 4  5  6
         # 7  8  -
        tile = puzzle_game.get_tile(3, 1)
        self.assertEqual(tile, 7)
        
    # # Kills puzzle_game.xǁPuzzleGameǁget_tile__mutmut_9: survived
    # # Testa o limite superior da coluna
    def test_get_tile_with_column_eq_to_limit(self):
        puzzle_game = PuzzleGame(3)
        # print(puzzle_game.board)
         # 1  2  3
         # 4  5  6
         # 7  8  -
        tile = puzzle_game.get_tile(1, 3)
        self.assertEqual(tile, 3)
    
    # # Kills puzzle_game.xǁPuzzleGameǁget_tile__mutmut_7: survived
    # # Testa o limite inferior da coluna
    def test_get_tile_with_column_eq_zero(self):
        puzzle_game = PuzzleGame(3)
        # print(puzzle_game.board)
         # 1  2  3
         # 4  5  6
         # 7  8  -
        with self.assertRaises(InvalidPositionException):
            tile = puzzle_game.get_tile(1, 0)
        
    
        
if __name__ == "__main__":
    unittest.main()
