import unittest
from dinheiro import Moeda, Dinheiro
from conta import Conta
from banco import Banco
from agencia import Agencia
from transacao import Transacao, Entrada, Saida


class TestConta(unittest.TestCase):
    def setUp(self):
        self.banco = Banco("BancoTeste", Moeda.BRL)
        self.agencia = Agencia("AgenciaTeste", 10, self.banco)

    def test_obter_formato_identificador_conta(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        conta = Conta("TitularTeste", 1, self.agencia)
        # RESULT VERIFICATION
        self.assertEqual("0001-2", conta.obter_identificador())
        # FIXTURE TEARDOWN

    def test_adicionar_saldo(self):
        # IMPLICIT INLINE FIXTURE SETUP
        self.conta.adicionar_transacao(Entrada(Dinheiro(Moeda.BRL, 20, 0)))
        # EXERCISE SUT
        saldo = self.conta.calcular_saldo().formatado()
        # RESULT VERIFICATION
        self.assertEqual("+20,00 BRL", saldo)
        # FIXTURE TEARDOWN

    def test_subtrair_saldo(self):
        # IMPLICIT INLINE FIXTURE SETUP
        self.conta.adicionar_transacao(Entrada(Dinheiro(Moeda.BRL, 20, 0)))
        self.conta.adicionar_transacao(Saida(Dinheiro(Moeda.BRL, 40, 0)))
        # EXERCISE SUT
        saldo = self.conta.calcular_saldo().formatado()
        # RESULT VERIFICATION
        self.assertEqual("-20,00 BRL", saldo)
        # FIXTURE TEARDOWN


if __name__ == "__main__":
    unittest.main()
