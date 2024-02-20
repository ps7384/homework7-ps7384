class Event:
    def __init__(self, name):
        self.name = name
        self.rsvps = []

    def add_rsvp(self, student):
        self.rsvps.append(student)

    def __str__(self):
        return f"Event: {self.name}"
