from Employee import Employee
from Occurrence import Occurrence, OType, Priority, State

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
            if employee.openOccurrences >= 10:
                raise ValueError("Funcionario possui 10 ocorrencias abertas")
            occurrence = Occurrence(self.occurrenceKey, employee, otype, priority, description)
            self.occurrenceKey += 1
            self.occurrences.append(occurrence)
            employee.openOccurrences += 1
            return occurrence
        raise ValueError("Funcionario fora do projeto")
    
    def modifyPriority(self, key, newPriority: Priority):
        try:
            occurrence = self.occurrences[key]
            if occurrence.state == State.CLOSED:
                raise ValueError("Ocorrencia fechada")
            self.occurrences[key].priority = newPriority
        except IndexError:
            raise IndexError("Index out of range")
        
    def modifyResponsible(self, key, newResponsible: Employee):
        try:
            if self.occurrences[key].state == State.CLOSED:
                raise ValueError("Ocorrencia fechada")
            if newResponsible in self.Employees:
                self.occurrences[key].employee = newResponsible
            else:
                raise ValueError("Funcionario fora do projeto")
        except IndexError:
            raise IndexError("Index out of range")

    def endOccurrence(self, key):
        try:
            if self.occurrences[key].state == State.OPEN:
                self.occurrences[key].state = State.CLOSED
                self.occurrences[key].employee.openOccurrences -= 1
            else:
                raise ValueError("Ocorrencia ja finalizada")
        except IndexError:
            raise IndexError("Index out of range")