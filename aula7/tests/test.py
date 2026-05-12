import unittest

class Test(unittest.TestCase):
    def setUp(self):
      pass
    
    def test_cria_empresa_W(self):
      result = Empresa("W")
      self.assertIsInstance(Empresa)


if __name__ == "__main__":
    unittest.main()
