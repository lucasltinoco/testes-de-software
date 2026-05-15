import unittest
from TestHelper import TestHelper
from Enterprise import Enterprise
from Employee import Employee
from Project import Project


class Test(unittest.TestCase):
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
        
    def test_incluir_projeto_na_empresa(self):
        EmpresaW = Enterprise("W")
        projeto2 = Project("2")
        EmpresaW.insertProject(projeto2)
        self.assertIn(projeto2, EmpresaW.Projects)
        
    def test_incluir_funcionario_em_projeto(self):
        (_, Carlos, ProjetoWeb) = TestHelper().cria_template_padrao()
        ProjetoWeb.insertEmployee(Carlos)
        self.assertIn(Carlos, ProjetoWeb.Employees)
        
    def test_insere_multiplos_funcionarios_com_nome_igual_na_empresa(self):
        Empresa = Enterprise("W")
        Joao = Employee("João")
        Joao2 = Employee("João")
        Empresa.insertEmployee(Joao)
        Empresa.insertEmployee(Joao2)
        self.assertEqual(2, len(Empresa.Employees))

    def test_busca_funcionario_por_nome_na_empresa(self):
        (Empresa, Carlos, _) = TestHelper().cria_template_padrao()
        Empresa.insertEmployee(Carlos)
        Carlos2 = Employee("Carlos")
        Empresa.insertEmployee(Carlos2)
        Gabriel = Employee("Gabriel")
        Empresa.insertEmployee(Gabriel)
        result = Empresa.findEmployees("Carlos")
        self.assertEqual(2, len(result))

    def test_nao_insere_mesmo_funcionario_duas_vezes_na_empresa(self):
        empresa = Enterprise("W")
        jose = Employee("José")
        empresa.insertEmployee(jose)
        empresa.insertEmployee(jose)
        self.assertEqual([jose], empresa.Employees)

    def test_nao_insere_mesmo_projeto_duas_vezes_na_empresa(self):
        empresa = Enterprise("W")
        projeto_web = Project("Projeto Web")
        empresa.insertProject(projeto_web)
        empresa.insertProject(projeto_web)
        self.assertEqual([projeto_web], empresa.Projects)

    def test_insere_funcionario_a_projeto_da_empresa(self):
        empresa = Enterprise("W")
        jose = Employee("José")
        projeto_web = Project("Projeto Web")
        empresa.insertEmployee(jose)
        empresa.insertProject(projeto_web)
        empresa.insertEmployeeInProject(jose, projeto_web)
        self.assertIn(jose, projeto_web.Employees)

    def test_nao_inclui_em_projeto_funcionario_que_nao_pertence_a_empresa(self):
        empresa = Enterprise("W")
        pedro = Employee("Pedro")
        projeto_engine = Project("Projeto Engine")
        empresa.insertProject(projeto_engine)
        with self.assertRaises(ValueError):
            empresa.insertEmployeeInProject(pedro, projeto_engine)
        self.assertNotIn(pedro, projeto_engine.Employees)

    def test_nao_inclui_funcionario_em_projeto_que_nao_pertence_a_empresa(self):
        empresa = Enterprise("W")
        pedro = Employee("Pedro")
        projeto_engine = Project("Projeto Engine")
        empresa.insertEmployee(pedro)
        with self.assertRaises(ValueError):
            empresa.insertEmployeeInProject(pedro, projeto_engine)
        self.assertNotIn(pedro, projeto_engine.Employees)

if __name__ == "__main__":
    unittest.main()
