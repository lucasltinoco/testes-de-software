import unittest
from Enterprise import Enterprise

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_cria_Enterprise_W(self):
        result = Enterprise("W")
        self.assertIsInstance(result, Enterprise)

    def test_cria_Funcionario_joao(self):
        funcionario = Employee("Joao")
        self.assertIsInstance(funcionario, Employee)

if __name__ == "__main__":
    unittest.main()
