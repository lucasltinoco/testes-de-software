import unittest
from Enterprise import Enterprise
from Employee import Employee

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_cria_Empresa_W(self):
        result = Enterprise("W")
        self.assertIsInstance(result, Enterprise)

    def test_cria_Funcionario_joao(self):
        funcionario = Employee("Joao")
        self.assertIsInstance(funcionario, Employee)
        
    def test_cria_Funcionario_na_Empresa(self):
        Empresa = Enterprise("W")
        Pedro = Employee("Pedro")
        Empresa.insertEmployee(Pedro)
        self.assertIn(Pedro, Empresa.Employees)

    def test_cria_Projeto(self):
        projeto = Project("1")
        self.assertIsInstance(projeto, Project)

if __name__ == "__main__":
    unittest.main()
