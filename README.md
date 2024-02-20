**RIT Campus Groups | RSVP System**

This Project aims at replicating RIT's Campus Groups RSVP System where for an Event university wide students can send in an RSVP to confirm their interest in an event.

The RIT Campus Groups | RSVP System enhances its functionality by including the Visitor pattern. The Visitor pattern involves sending confirmation emails to students who have RSVP'd. We use the ConfirmationEmailVisitor class as a visitor. The guest elaborates on the reason why students
who have confirmed their attendance receive email notifications. The system utilizes the Visitor pattern to apply the ConfirmationEmailVisitor on the student object during event RSVP. Following the visit, the student is sent a confirmation email.The Visitor architecture
allows us to do several operations on students who have RSVP'd without making changes to the student class. This encourages a design that is simple to clean.


**Features** 
1. Student RSVP: Students can easily RSVP for events by providing their name and email address.
2. Administrator View: Administrators can view the list of students who have RSVP'd for each event.
3. Confirmation Emails: Students receive confirmation emails upon successful RSVP for an event.
