import unittest
from dinheiro import Dinheiro, Moeda


class TestDinheiro(unittest.TestCase):
    def setUp(self):
        pass

    def test_quantia_em_escala_de_dez_reais_cinquenta_centavos(self):
        # INLINE FIXTURE SETUP
        dez_reais_cinquenta_centavos = Dinheiro(Moeda.BRL, 10, 50)
        # EXERCISE SUT
        quantia_em_escala = dez_reais_cinquenta_centavos.obter_quantia_em_escala()
        # RESULT VERIFICATION
        self.assertEqual(1050, quantia_em_escala)
        # FIXTURE TEARDOWN

    def test_negativo_de_dez_reais(self):
        # INLINE FIXTURE SETUP
        dez_reais = Dinheiro(Moeda.BRL, 10, 0)
        # EXERCISE SUT
        valor_dez_negativo = dez_reais.negativo()  # retorna um valor monetario
        # RESULT VERIFICATION
        self.assertTrue(valor_dez_negativo.negativo())
        self.assertEqual(
            1000, int(valor_dez_negativo.obter_quantia().obter_quantia_em_escala())
        )
        # FIXTURE TEARDOWN

    def test_formatacao_de_dez_reais_cinquenta_centavos(self):
        # INLINE FIXTURE SETUP
        dez_reais_cinquenta_centavos = Dinheiro(Moeda.BRL, 10, 50)
        # EXERCISE SUT
        formatacao = dez_reais_cinquenta_centavos.formatado()
        # RESULT VERIFICATION
        self.assertEqual("10,50 BRL", formatacao)
        # FIXTURE TEARDOWN

    def test_formatacao_de_dez_reais_cinquenta_centavos_negativo(self):
        # INLINE FIXTURE SETUP
        dez_reais_cinquenta_centavos = Dinheiro(Moeda.BRL, 10, 50)
        dez_reais_cinquenta_centavos_negativo = dez_reais_cinquenta_centavos.negativo()
        # EXERCISE SUT
        formatacao = dez_reais_cinquenta_centavos_negativo.formatado()
        # RESULT VERIFICATION
        self.assertEqual("-10,50 BRL", formatacao)
        # FIXTURE TEARDOWN

    def test_formatacao_zero(self):
        # INLINE FIXTURE SETUP
        zero_reais = Dinheiro(Moeda.BRL, 0, 0)
        # EXERCISE SUT
        formatacao = zero_reais.formatado()
        # RESULT VERIFICATION
        self.assertEqual("0,00", formatacao)
        # FIXTURE TEARDOWN


if __name__ == "__main__":
    unittest.main()
