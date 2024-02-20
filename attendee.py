class Attendee:
    def accept(self, visitor):
        raise NotImplementedError("Subclasses must implement abstract method")

class Student(Attendee):
    def __init__(self, name, email, major):
        self.name = name
        self.email = email
        self.major = major

    def accept(self, visitor):
        visitor.visit_student(self)

class Faculty(Attendee):
    def __init__(self, name, email, department):
        self.name = name
        self.email = email
        self.department = department

    def accept(self, visitor):
        visitor.visit_faculty(self)

class Alumni(Attendee):
    def __init__(self, name, email, grad_year):
        self.name = name
        self.email = email
        self.grad_year = grad_year

    def accept(self, visitor):
        visitor.visit_alumni(self)
