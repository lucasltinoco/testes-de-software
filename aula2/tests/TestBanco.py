import unittest
from dinheiro import Moeda
from conta import Conta
from banco import Banco
from agencia import Agencia

from TestHelper import TestHelper


class TestBanco(unittest.TestCase):
    def setUp(self):
        self.banco = Banco("BancoTeste", Moeda.BRL)

    def test_criacao_agencias(self):
        # IMPLICIT INLINE FIXTURE SETUP
        # EXERCISE SUT
        agencias_criadas = []
        agencias_criadas.append(self.banco.criar_agencia("Agencia0"))
        agencias_criadas.append(self.banco.criar_agencia("Agencia1"))
        agencias_criadas.append(self.banco.criar_agencia("Agencia2"))
        agencias_criadas.append(self.banco.criar_agencia("Agencia3"))
        # RESULT VERIFICATION
        agencias_recuperadas = []
        agencias_recuperadas.append(self.banco.obter_agencia("Agencia0"))
        agencias_recuperadas.append(self.banco.obter_agencia("Agencia1"))
        agencias_recuperadas.append(self.banco.obter_agencia("Agencia2"))
        agencias_recuperadas.append(self.banco.obter_agencia("Agencia3"))
        self.assertEqual(agencias_criadas, agencias_recuperadas)
        # FIXTURE TEARDOWN

    def test_obter_agencia_inexistente(self):
        # IMPLICIT INLINE FIXTURE SETUP
        # EXERCISE SUT
        agencia_inexistente = self.banco.obter_agencia("AgenciaInexistente")
        # RESULT VERIFICATION
        self.assertIsNone(agencia_inexistente)
        # FIXTURE TEARDOWN
      
    def test_obter_agencia_criada(self):
        # IMPLICIT INLINE FIXTURE SETUP
        agencia_criada = self.banco.criar_agencia("AgenciaTeste")
        # EXERCISE SUT
        agencia_obtida = self.banco.obter_agencia("AgenciaTeste")
        # RESULT VERIFICATION
        self.assertEqual(agencia_criada, agencia_obtida)
        # FIXTURE TEARDOWN


if __name__ == "__main__":
    unittest.main()
