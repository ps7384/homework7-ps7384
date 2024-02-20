class Visitor:
    def visit_student(self, student):
        pass

    def visit_faculty(self, faculty):
        pass

    def visit_alumni(self, alumni):
        pass

class SignUpVisitor(Visitor):
    def visit_student(self, student):
        print(f"{student.name} ({student.email}, {student.major}) RSVP'd for the event")

    def visit_faculty(self, faculty):
        print(f"{faculty.name} ({faculty.email}, {faculty.department}) RSVP'd for the event")

    def visit_alumni(self, alumni):
        print(f"{alumni.name} ({alumni.email}, {alumni.grad_year}) RSVP'd for the event")
