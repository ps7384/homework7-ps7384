from visitor import ConfirmationEmailVisitor

class EnrollmentSystem:
    def __init__(self):
        self.students = []
        self.event = None

    def add_student(self, student):
        self.students.append(student)

    def set_event(self, event):
        self.event = event

    def rsvp_for_event(self, student_email):
        student = next((s for s in self.students if s.email == student_email), None)
        if student:
            self.event.add_rsvp(student)
            print(f"{student.name} RSVP'd for the event.")
            return student
        else:
            print("Student not found.")
            return None

    def show_rsvps(self):
        print(f"RSVPs for {self.event.name}:")
        for student in self.event.rsvps:
            print(student)

    def send_confirmation_emails(self):
        confirmation_email_visitor = ConfirmationEmailVisitor()
        for student in self.event.rsvps:
            confirmation_email_visitor.visit_student(student)
