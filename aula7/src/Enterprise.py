from Employee import Employee

class Enterprise():
    def __init__(self, name):
        self.name = "W"
        self.Employees = []
    
    def insertEmployee(self, employee: Employee):
        self.Employees.append(employee)