from student import Student
from event import Event
from enrollment_system import EnrollmentSystem

# Create students
student1 = Student("Paul", "ps@rit.edu")
student2 = Student("Brad", "bb@rit.edu")
student3 = Student("Chloe", "cs@rit.edu")

event = Event("RIT Campus Groups | RSVP")


# Create enrollment system
enrollment_system = EnrollmentSystem()

# Add students to the enrollment system
enrollment_system.add_student(student1)
enrollment_system.add_student(student2)
enrollment_system.add_student(student3)

# Set the event in the enrollment system
enrollment_system.set_event(event)

# RSVP for the event
enrollment_system.rsvp_for_event("ps@rit.edu")
enrollment_system.rsvp_for_event("bb@rit.edu")
enrollment_system.rsvp_for_event("cc@rit.edu")  # Non-existent student

# Show RSVPs
enrollment_system.show_rsvps()

# Send confirmation emails
enrollment_system.send_confirmation_emails()
