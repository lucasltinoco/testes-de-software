import unittest
from Empresa import Empresa

class Test(unittest.TestCase):
    def setUp(self):
      pass
    
    def test_cria_empresa_W(self):
      result = Empresa("W")
      self.assertIsInstance(result, Empresa)


if __name__ == "__main__":
    unittest.main()
