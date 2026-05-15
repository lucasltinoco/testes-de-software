from Employee import Employee

class Project:
    def __init__(self, id):
        self.id = id
        self.Employees = []
        
    def insertEmployee(self, employee: Employee):
        if employee not in self.Employees:
            self.Employees.append(employee)
