import unittest
from dinheiro import Moeda, Dinheiro
from conta import Conta
from banco import Banco
from agencia import Agencia
from transacao import Transacao, Entrada, Saida
from sistema_bancario import SistemaBancario


class TestSistemaBancario(unittest.TestCase):
    def setUp(self):
        self.sistema_bancario = SistemaBancario()

    def test_criar_bancos(self):
        # IMPLICIT INLINE FIXTURE SETUP
        bancos_criados = []
        for i in range(3):
            bancos_criados.append(
                self.sistema_bancario.criar_banco(f"Banco {i}", Moeda.BRL)
            )
        # EXERCISE SUT
        bancos_recuperados = self.sistema_bancario.obter_bancos()
        # RESULT VERIFICATION
        self.assertEqual(bancos_criados, bancos_recuperados)
        # FIXTURE TEARDOWN

    def test_deposito_no_banco(self):
        # IMPLICIT INLINE FIXTURE SETUP
        banco = self.sistema_bancario.criar_banco("Banco Teste", Moeda.BRL)
        agencia = banco.criar_agencia("Agencia Teste")
        conta = agencia.criar_conta("Titular Teste")
        # EXERCISE SUT
        self.sistema_bancario.depositar(conta, Dinheiro(Moeda.BRL, 100, 0))
        # RESULT VERIFICATION
        self.assertEqual("+100,00 BRL", conta.calcular_saldo().formatado())
        # FIXTURE TEARDOWN

    def test_saque_do_banco(self):
        # IMPLICIT INLINE FIXTURE SETUP
        banco = self.sistema_bancario.criar_banco("Banco Teste", Moeda.BRL)
        agencia = banco.criar_agencia("Agencia Teste")
        conta = agencia.criar_conta("Titular Teste")
        self.sistema_bancario.depositar(conta, Dinheiro(Moeda.BRL, 100, 0))
        # EXERCISE SUT
        self.sistema_bancario.sacar(conta, Dinheiro(Moeda.BRL, 40, 0))
        # RESULT VERIFICATION
        self.assertEqual("+60,00 BRL", conta.calcular_saldo().formatado())
        # FIXTURE TEARDOWN

    def test_transferir_entre_bancos(self):
        # IMPLICIT INLINE FIXTURE SETUP
        banco_origem = self.sistema_bancario.criar_banco("Banco Origem", Moeda.BRL)
        agencia_origem = banco_origem.criar_agencia("Agencia Origem")
        conta_origem = agencia_origem.criar_conta("Titular Origem")
        self.sistema_bancario.depositar(conta_origem, Dinheiro(Moeda.BRL, 100, 0))

        banco_destino = self.sistema_bancario.criar_banco("Banco Destino", Moeda.BRL)
        agencia_destino = banco_destino.criar_agencia("Agencia Destino")
        conta_destino = agencia_destino.criar_conta("Titular Destino")
        # EXERCISE SUT
        self.sistema_bancario.transferir(
            conta_origem, conta_destino, Dinheiro(Moeda.BRL, 40, 0)
        )
        # RESULT VERIFICATION
        self.assertEqual("+60,00 BRL", conta_origem.calcular_saldo().formatado())
        self.assertEqual("+40,00 BRL", conta_destino.calcular_saldo().formatado())
        # FIXTURE TEARDOWN


if __name__ == "__main__":
    unittest.main()
