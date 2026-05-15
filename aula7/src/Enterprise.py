import re

from Employee import Employee
from Project import Project

class Enterprise():
    def __init__(self, name):
        self.name = "W"
        self.Employees = []
        self.Projects = []
    
    def insertEmployee(self, employee: Employee):
        if employee not in self.Employees:
            self.Employees.append(employee)
        
    def insertProject(self, project: Project):
        if project not in self.Projects:
            self.Projects.append(project)
        
    def findEmployees(self, string: str):
        results = [e for e in self.Employees if re.search(string, e.name)]
        return results

    def insertEmployeeInProject(self, employee: Employee, project: Project):
        project.insertEmployee(employee)
