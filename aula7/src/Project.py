from Employee import Employee
from Occurrence import Occurrence, OType, Priority

class Project:
    def __init__(self, id):
        self.id = id
        self.Employees = []
        self.occurrences = []
        self.occurrenceKey = 0
        
    def insertEmployee(self, employee: Employee):
        if employee not in self.Employees:
            self.Employees.append(employee)
            
    def addOccurrence(self, employee: Employee, otype: OType, priority: Priority, description: str):
        if employee in self.Employees:
            occurrence = Occurrence(self.occurrenceKey, employee, otype, priority, description)
            self.occurrenceKey += 1
            self.occurrences.append(occurrence)
            return occurrence
        raise ValueError("Funcionario fora do projeto")
    
    def modifyPriority(self, key, newPriority: Priority):
        try:
            self.occurrences[key].priority = newPriority
        except IndexError:
            raise IndexError("Index out of range")
        
    def modifyResponsible(self, key, newResponsible: Employee):
        try:
            if newResponsible in self.Employees:
                self.occurrences[key].employee = newResponsible
            else:
                raise ValueError("Funcionario fora do projeto")
        except IndexError:
            raise IndexError("Index out of range")
