from Enterprise import Enterprise
from Employee import Employee
from Project import Project

class TestHelper():
  def cria_template_padrao(self):
      Empresa = Enterprise("W")
      Carlos = Employee("Carlos")
      ProjetoWeb = Project("1")
      return (Empresa, Carlos, ProjetoWeb)
      
