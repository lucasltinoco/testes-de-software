import unittest
from dinheiro import ValorMonetario, Dinheiro, Moeda


class TestValorMonetario(unittest.TestCase):
    def setUp(self):
        pass

    def test_moeda_invalida_euro(self):
        # INLINE FIXTURE SETUP
        # EXERCISE SUT
        with self.assertRaises(AttributeError):
            dez_reais_cinquenta = ValorMonetario("EUR", 10.50)
        # RESULT VERIFICATION
        # FIXTURE TEARDOWN

    def test_somar_valor(self):
        # INLINE FIXTURE SETUP
        um_real_dez = ValorMonetario(Moeda.BRL, 110)
        vinte_reais_trinta = Dinheiro(Moeda.BRL, 20, 30)
        # EXERCISE SUT
        soma = um_real_dez.somar(vinte_reais_trinta)
        # RESULT VERIFICATION
        self.assertEqual("+21,40 BRL", soma.formatado())
        # FIXTURE TEARDOWN

    def test_subtrair_valor_resultado_negativo(self):
        # INLINE FIXTURE SETUP
        um_real_dez = ValorMonetario(Moeda.BRL, 110)
        vinte_reais_trinta = Dinheiro(Moeda.BRL, 20, 30)
        # EXERCISE SUT
        subtracao = um_real_dez.subtrair(vinte_reais_trinta)
        # RESULT VERIFICATION
        self.assertEqual("-19,20 BRL", subtracao.formatado())
        # FIXTURE TEARDOWN


if __name__ == "__main__":
    unittest.main()
