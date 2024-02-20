from abc import ABC, abstractmethod
from student import Student

class Visitor(ABC):
    @abstractmethod
    def visit_student(self, student: Student):
        pass

class ConfirmationEmailVisitor(Visitor):
    def visit_student(self, student: Student):
        print(f"Sending confirmation email to {student.email}")
