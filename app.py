import tkinter as tk
from tkinter import ttk
from event import Event
from attendee import Student, Faculty, Alumni
from visitor import SignUpVisitor

def set_style():
    return {
        "Label": {
            "font": ("Helvetica", 12),
            "foreground": "black",
            "background": "white",
            "padding": (5, 5)
        },
        "Entry": {
            "font": ("Helvetica", 12),
            "foreground": "black",
            "background": "white",
            "borderwidth": 1,
            "relief": "solid",
            "padding": (5, 5)
        },
        "Button": {
            "font": ("Helvetica", 12),
            "foreground": "white",
            "background": "blue",
            "borderwidth": 0,
            "relief": "flat",
            "padding": (10, 5)
        },
        "Combobox": {
            "font": ("Helvetica", 12),
            "foreground": "black",
            "background": "white",
            "padding": (5, 5)
        },
        "Text": {
            "font": ("Helvetica", 12),
            "foreground": "black",
            "background": "white",
            "borderwidth": 1,
            "relief": "solid",
            "padding": (5, 5)
        }
    }

class RSVPAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rochester Institute of Technology | RSVP")

        # Set styles
        self.set_styles()

        # Create widgets
        self.create_widgets()

    def set_styles(self):
        style = ttk.Style()
        for widget, properties in set_style().items():
            style.configure(widget, **properties)

    def create_widgets(self):
        # Name entry
        tk.Label(self.root, text="Name:").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        # Email entry
        tk.Label(self.root, text="RIT Email:").pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        # Major entry
        tk.Label(self.root, text="Major:").pack()
        self.major_entry = tk.Entry(self.root)
        self.major_entry.pack()

        # User selection
        self.user_type = tk.StringVar()
        self.user_type.set("Student")  # Default selection

        # Label
        tk.Label(self.root, text="Select Attendee Type:").pack()

        # Combobox for attendee type selection
        self.user_type_combobox = ttk.Combobox(self.root, textvariable=self.user_type, values=["Student", "Faculty", "Alumni"])
        self.user_type_combobox.pack()

        # RSVP Button
        tk.Button(self.root, text="RSVP", command=self.rsvp_event).pack()

        # Output Text
        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.pack()

    def rsvp_event(self):
        # Get input values
        name = self.name_entry.get()
        email = self.email_entry.get()
        major = self.major_entry.get()

        # Get selected attendee type
        attendee_type = self.user_type.get()

        # Create attendee based on selection
        if attendee_type == "Student":
            attendee = Student(name, email, major)
        elif attendee_type == "Faculty":
            attendee = Faculty(name, email, major)
        elif attendee_type == "Alumni":
            attendee = Alumni(name, email, major)

        # Add attendee to the event
        self.event.attendees.append(attendee)

        # Perform RSVP using Visitor pattern
        signup_visitor = SignUpVisitor()
        attendee.accept(signup_visitor)

        # Update output text
        self.output_text.insert(tk.END, f"{name} ({attendee_type}) RSVP'd for the event\n")
        self.clear_fields()

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.major_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = RSVPAppGUI(root)
    root.mainloop()
