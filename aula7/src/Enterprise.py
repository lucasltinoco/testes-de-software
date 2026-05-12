from Employee import Employee
from Project import Project

class Enterprise():
    def __init__(self, name):
        self.name = "W"
        self.Employees = []
        self.Projects = []
    
    def insertEmployee(self, employee: Employee):
        self.Employees.append(employee)
        
    def insertProject(self, project: Project):
        self.Projects.append(project)