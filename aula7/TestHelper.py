from pathlib import Path
import sys

root_dir = Path(__file__).resolve().parents[1]
src_dir = root_dir / "src"

sys.path.insert(0, str(src_dir))

from Enterprise import Enterprise
from Employee import Employee
from Project import Project

class TestHelper():
  def cria_template_padrao(self):
      Empresa = Enterprise("W")
      Carlos = Employee("Carlos")
      ProjetoWeb = Project("1")
      return (Empresa, Carlos, ProjetoWeb)
      
