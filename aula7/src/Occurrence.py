import re
from enum import Enum

from Employee import Employee


class OType(Enum):
    BUG = "Bug"
    TASK = "Tarefa"
    REFAC = "Refatoracao"


class Priority(Enum):
    HIGH = "Alta"
    MEDIUM = "Media"
    LOW = "Baixa"
    
class State(Enum):
    OPEN = "Aberta"
    CLOSED = "Fechada"


class Occurrence:
    def __init__(
        self, key: int, employee: Employee, otype: OType, priority: Priority, description: str
    ):
        self.key = key
        self.employee = employee
        self.otype = otype
        self.priority = priority
        self.description = description
        self.state = State.OPEN
