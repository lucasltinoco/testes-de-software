from pathlib import Path
import sys

root_dir = Path(__file__).resolve().parents[1]
src_dir = root_dir / "src"

sys.path.insert(0, str(src_dir))

import unittest
from TestHelper import TestHelper
from Enterprise import Enterprise
from Employee import Employee
from Project import Project
from Occurrence import State, OType, Priority


class Test(unittest.TestCase):
    def test_cria_empresa_w(self):
        result = Enterprise("W")
        self.assertIsInstance(result, Enterprise)

    def test_cria_funcionario_joao(self):
        funcionario = Employee("Joao")
        self.assertIsInstance(funcionario, Employee)
        
    def test_cria_funcionario_na_empresa(self):
        empresa = Enterprise("W")
        pedro = Employee("Pedro")
        empresa.insertEmployee(pedro)
        self.assertIn(pedro, empresa.Employees)

    def test_cria_projeto(self):
        projeto = Project("1")
        self.assertIsInstance(projeto, Project)
        
    def test_incluir_projeto_na_empresa(self):
        empresa_w = Enterprise("W")
        projeto2 = Project("2")
        empresa_w.insertProject(projeto2)
        self.assertIn(projeto2, empresa_w.Projects)
        
    def test_incluir_funcionario_em_projeto(self):
        (_, carlos, projeto_web) = TestHelper().cria_template_padrao()
        projeto_web.insertEmployee(carlos)
        self.assertIn(carlos, projeto_web.Employees)
        
    def test_insere_multiplos_funcionarios_com_nome_igual_na_empresa(self):
        empresa = Enterprise("W")
        joao = Employee("João")
        joao2 = Employee("João")
        empresa.insertEmployee(joao)
        empresa.insertEmployee(joao2)
        self.assertEqual(2, len(empresa.Employees))

    def test_busca_funcionario_por_nome_na_empresa(self):
        (empresa, carlos, _) = TestHelper().cria_template_padrao()
        empresa.insertEmployee(carlos)
        carlos2 = Employee("Carlos")
        empresa.insertEmployee(carlos2)
        gabriel = Employee("Gabriel")
        empresa.insertEmployee(gabriel)
        result = empresa.findEmployees("Carlos")
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

    def test_funcionario_pode_trabalhar_em_varios_projetos(self):
        empresa = Enterprise("W")
        ana = Employee("Ana")
        projeto_web = Project("Projeto Web")
        projeto_mobile = Project("Projeto Mobile")
        empresa.insertEmployee(ana)
        empresa.insertProject(projeto_web)
        empresa.insertProject(projeto_mobile)
        empresa.insertEmployeeInProject(ana, projeto_web)
        empresa.insertEmployeeInProject(ana, projeto_mobile)
        self.assertIn(ana, projeto_web.Employees)
        self.assertIn(ana, projeto_mobile.Employees)

    def test_projeto_pode_ter_varios_funcionarios(self):
        empresa = Enterprise("W")
        jose = Employee("José")
        maria = Employee("Maria")
        projeto_web = Project("Projeto Web")
        empresa.insertEmployee(jose)
        empresa.insertEmployee(maria)
        empresa.insertProject(projeto_web)
        empresa.insertEmployeeInProject(jose, projeto_web)
        empresa.insertEmployeeInProject(maria, projeto_web)
        self.assertIn(jose, projeto_web.Employees)
        self.assertIn(maria, projeto_web.Employees)

    def test_nao_insere_mesmo_funcionario_duas_vezes_no_mesmo_projeto(self):
        empresa = Enterprise("W")
        jose = Employee("José")
        projeto_web = Project("Projeto Web")
        empresa.insertEmployee(jose)
        empresa.insertProject(projeto_web)
        empresa.insertEmployeeInProject(jose, projeto_web)
        empresa.insertEmployeeInProject(jose, projeto_web)
        self.assertEqual([jose], projeto_web.Employees)

    def test_busca_funcionario_por_nome_retorna_funcionarios_corretos(self):
        empresa = Enterprise("W")
        carlos = Employee("Carlos")
        carlos_segundo = Employee("Carlos")
        gabriel = Employee("Gabriel")
        empresa.insertEmployee(carlos)
        empresa.insertEmployee(carlos_segundo)
        empresa.insertEmployee(gabriel)
        resultado = empresa.findEmployees("Carlos")
        self.assertIn(carlos, resultado)
        self.assertIn(carlos_segundo, resultado)
        self.assertNotIn(gabriel, resultado)

    def test_busca_funcionario_inexistente_retorna_lista_vazia(self):
        empresa = Enterprise("W")
        jose = Employee("José")
        empresa.insertEmployee(jose)
        resultado = empresa.findEmployees("Maria")
        self.assertEqual([], resultado)

#Parte 2
 
    def test_cria_ocorrencia_em_projeto(self):
        (empresa, carlos, projeto_web) = TestHelper().cria_template_padrao()
        empresa.insertEmployee(carlos)
        empresa.insertProject(projeto_web)
        empresa.insertEmployeeInProject(carlos, projeto_web)
        occurrence = projeto_web.addOccurrence(carlos, "Bug", "Media", "Vazamento de memoria")
        self.assertIn(occurrence, projeto_web.occurrences)

    def test_cria_ocorrencia_com_responsavel_fora_do_projeto(self):
        (empresa, carlos, projeto_web) = TestHelper().cria_template_padrao()
        empresa.insertEmployee(carlos)
        empresa.insertProject(projeto_web)
        with self.assertRaises(ValueError):
            occurrence = projeto_web.addOccurrence(carlos, "Bug", "Media", "Vazamento de memoria")
            self.assertNotIn(occurrence, projeto_web.occurrences)
            
    def test_modifica_prioridade_de_ocorrencia(self):
        (empresa, carlos, projeto_web) = TestHelper().cria_template_padrao()
        empresa.insertEmployee(carlos)
        empresa.insertProject(projeto_web)
        empresa.insertEmployeeInProject(carlos, projeto_web)
        occurrence = projeto_web.addOccurrence(carlos, "Bug", "Media", "Vazamento de memoria")
        projeto_web.modifyPriority(occurrence.key, "Alta")
        self.assertEqual(projeto_web.occurrences[occurrence.key].priority, "Alta")

    def test_modifica_prioridade_de_ocorrencia_inexistente(self):
        (empresa, carlos, projeto_web) = TestHelper().cria_template_padrao()
        empresa.insertEmployee(carlos)
        empresa.insertProject(projeto_web)
        empresa.insertEmployeeInProject(carlos, projeto_web)
        occurrence = projeto_web.addOccurrence(carlos, "Bug", "Media", "Vazamento de memoria")
        with self.assertRaises(IndexError):
            projeto_web.modifyPriority(1, "Alta")
            self.assertEqual(projeto_web.occurrences[occurrence.key].priority, "Media")
            
    def test_modifica_responsavel_de_ocorrencia(self):
        (empresa, carlos, projeto_web) = TestHelper().cria_template_padrao()
        maria = Employee("Maria")
        empresa.insertEmployee(carlos)
        empresa.insertEmployee(maria)
        empresa.insertProject(projeto_web)
        empresa.insertEmployeeInProject(carlos, projeto_web)
        empresa.insertEmployeeInProject(maria, projeto_web)
        occurrence = projeto_web.addOccurrence(carlos, "Bug", "Media", "Vazamento de memoria")
        projeto_web.modifyResponsible(occurrence.key, maria)
        self.assertEqual(projeto_web.occurrences[occurrence.key].employee, maria)

    def test_modifica_responsavel_de_ocorrencia_inexistente(self):
        (empresa, carlos, projeto_web) = TestHelper().cria_template_padrao()
        maria = Employee("Maria")
        empresa.insertEmployee(carlos)
        empresa.insertEmployee(maria)
        empresa.insertProject(projeto_web)
        empresa.insertEmployeeInProject(carlos, projeto_web)
        empresa.insertEmployeeInProject(maria, projeto_web)
        occurrence = projeto_web.addOccurrence(carlos, "Bug", "Media", "Vazamento de memoria")
        with self.assertRaises(IndexError):
            projeto_web.modifyResponsible(1, maria)
            self.assertEqual(projeto_web.occurrences[occurrence.key].employee, carlos)
            
    def test_modifica_responsavel_de_ocorrencia_com_funcionario_fora_do_projeto(self):
        (empresa, carlos, projeto_web) = TestHelper().cria_template_padrao()
        maria = Employee("Maria")
        empresa.insertEmployee(carlos)
        empresa.insertEmployee(maria)
        empresa.insertProject(projeto_web)
        empresa.insertEmployeeInProject(carlos, projeto_web)
        occurrence = projeto_web.addOccurrence(carlos, "Bug", "Media", "Vazamento de memoria")
        with self.assertRaises(ValueError):
            projeto_web.modifyResponsible(occurrence.key, maria)
        self.assertEqual(projeto_web.occurrences[occurrence.key].employee, carlos)
        
    def test_finalizar_ocorrencia(self):
        (empresa, carlos, projeto_web) = TestHelper().cria_template_padrao()
        empresa.insertEmployee(carlos)
        empresa.insertProject(projeto_web)
        empresa.insertEmployeeInProject(carlos, projeto_web)
        occurrence = projeto_web.addOccurrence(carlos, "Bug", "Media", "Vazamento de memoria")
        projeto_web.endOccurrence(occurrence.key)
        self.assertEqual(projeto_web.occurrences[occurrence.key].state, State.CLOSED)
        
    def test_finalizar_ocorrencia_inexistente(self):
        (empresa, carlos, projeto_web) = TestHelper().cria_template_padrao()
        empresa.insertEmployee(carlos)
        empresa.insertProject(projeto_web)
        empresa.insertEmployeeInProject(carlos, projeto_web)
        occurrence = projeto_web.addOccurrence(carlos, "Bug", "Media", "Vazamento de memoria")
        with self.assertRaises(IndexError):
            projeto_web.endOccurrence(1)
            self.assertEqual(projeto_web.occurrences[occurrence.key].state, State.OPEN)
            
    def test_finalizar_ocorrencia_ja_finalizada(self):
        (empresa, carlos, projeto_web) = TestHelper().cria_template_padrao()
        empresa.insertEmployee(carlos)
        empresa.insertProject(projeto_web)
        empresa.insertEmployeeInProject(carlos, projeto_web)
        occurrence = projeto_web.addOccurrence(carlos, "Bug", "Media", "Vazamento de memoria")
        projeto_web.endOccurrence(occurrence.key)
        self.assertRaises(ValueError, projeto_web.endOccurrence, occurrence.key)

    def test_ocorrencia_criada_possui_chave_resumo_tipo_prioridade_responsavel_e_estado_aberto(self):
        empresa = Enterprise("W")
        ana = Employee("Ana")
        projeto_web = Project("Projeto Web")
        empresa.insertEmployee(ana)
        empresa.insertProject(projeto_web)
        empresa.insertEmployeeInProject(ana, projeto_web)
        ocorrencia = projeto_web.addOccurrence(ana, OType.BUG, Priority.MEDIUM, "Vazamento de memoria")

        self.assertEqual(0, ocorrencia.key)
        self.assertEqual("Vazamento de memoria", ocorrencia.description)
        self.assertEqual(OType.BUG, ocorrencia.otype)
        self.assertEqual(Priority.MEDIUM, ocorrencia.priority)
        self.assertEqual(ana, ocorrencia.employee)
        self.assertEqual(State.OPEN, ocorrencia.state)
        self.assertIn(ocorrencia, projeto_web.occurrences)

    def test_ocorrencias_do_mesmo_projeto_possuem_chaves_unicas(self):
        empresa = Enterprise("W")
        ana = Employee("Ana")
        projeto_web = Project("Projeto Web")

        empresa.insertEmployee(ana)
        empresa.insertProject(projeto_web)
        empresa.insertEmployeeInProject(ana, projeto_web)

        vazamento_memoria = projeto_web.addOccurrence(ana,OType.BUG,Priority.HIGH,"Vazamento de memoria")
        atualizar_layout = projeto_web.addOccurrence(ana,OType.TASK,Priority.MEDIUM,"Atualizar layout da tela inicial")

        self.assertNotEqual(vazamento_memoria.key, atualizar_layout.key)
        self.assertIn(vazamento_memoria, projeto_web.occurrences)
        self.assertIn(atualizar_layout, projeto_web.occurrences)


if __name__ == "__main__":
    unittest.main()
