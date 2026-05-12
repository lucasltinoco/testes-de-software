from Employee import Employee

class Project:
    def __init__(self, id):
        self.id = id
        self.Employees = []
        
    def insertEmployee(self, employee: Employee):
        self.Employees.append(employee)
