import unittest
from dinheiro import Moeda
from conta import Conta
from banco import Banco
from agencia import Agencia

from TestHelper import TestHelper


class TestAgencia(unittest.TestCase):
    def setUp(self):
        self.banco = Banco("BancoTeste", Moeda.BRL)
        self.agencia = Agencia("AgenciaTeste", 10, self.banco)

    def test_criacao_conta_do_titular_teste(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        conta = Conta("TitularTeste", 8, self.agencia)
        # RESULT VERIFICATION
        self.assertEqual("TitularTeste", conta.titular)
        self.assertEqual(self.agencia, conta.agencia)
        # FIXTURE TEARDOWN

    def test_obter_formato_identificador_agencia(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        agencia = Agencia("AgenciaTeste2", 10, self.banco)
        # RESULT VERIFICATION
        self.assertEqual("010", agencia.obter_identificador())
        # FIXTURE TEARDOWN

    def test_criacao_contas(self):
        # IMPLICIT and DELEGATED FIXTURE SETUP
        # EXERCISE SUT
        contas = TestHelper().make_n_contas(5, self.agencia)
        # RESULT VERIFICATION
        self.assertEqual(contas, self.agencia.obter_contas())
        # FIXTURE TEARDOWN


if __name__ == "__main__":
    unittest.main()
